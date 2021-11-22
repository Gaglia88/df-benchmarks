import importlib
import time
import docker
import os
import json
import psutil
import colors
import threading
import argparse

def create_algo(definition):
    """
    Create a new instance of the requested algorithm
    """
    module = importlib.import_module(definition['module'])
    constructor = getattr(module, definition['constructor'])
    return constructor(*definition['constructor_args'])
    
def load_datasets():
    """
    Load all the datasets definitions
    """
    f = open('datasets/datasets.json',"rt")
    data = json.load(f)
    datasets = {}
    for r in data:
        datasets[r['name']] = r
    return datasets
    
def load_algorithms():
    """
    Load all the algorithms definitions
    """
    f = open('df_benchmark/algorithms/algorithms.json',"rt")
    data = json.load(f)
    datasets = {}
    for r in data:
        datasets[r['name']] = r
    return datasets
    
def load_tests(path):
    """
    Load the tests for a specified dataset
    """
    f = open(path, "rt")
    return  json.load(f)

def get_logger(dataset, algorithm):
    """
    Create a log file for the specified dataset and algorithm
    """
    out_path = os.path.join('results', dataset)
    
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    
    out_log = os.path.join(out_path, algorithm+".csv")
    log = open(out_log, "wt")
    log.write("operation,time,mem\n")
    return log

def run_algo():
    """
        Runs an algorithm on local machine
    """
    #Load available algorithms
    algorithms = load_algorithms()
    
    #Load available datasets
    datasets = load_datasets()
    
    #Set up argument parset
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--algorithm',
        choices=algorithms.keys(),
        help='Algorithm name',
        required=True)
    parser.add_argument(
        '--dataset',
        choices=datasets.keys(),
        help='Dataset name',
        required=True)
    args = parser.parse_args()
    
    #Load the current algorithm
    algo = create_algo(algorithms[args.algorithm])
    
    #Create log file
    log = get_logger(dataset, args.algorithm)
    
    #Load the tests to perform on the dataset
    tests = load_tests(datasets[args.dataset]['tests'])
    
    #Load the data
    print("Load data")
    mstart = algo.get_memory_usage()
    tstart = time.time()
    algo.load_dataset(datasets[args.dataset]['path'], datasets[args.dataset]['type'], sep=',')
    t = time.time()-tstart
    m = algo.get_memory_usage()-mstart
    log.write("load_data,"+str(t)+","+str(m)+"\n")
    
    #Execute each test on the dataset
    for test in tests:
        print("Running "+test['method'])
        mstart = algo.get_memory_usage()
        tstart = time.time()
        getattr(algo, test['method'])(test['input'])
        t = time.time()-tstart
        m = algo.get_memory_usage()-mstart
        log.write(test['method']+","+str(t)+","+str(m)+"\n")
        
    
    print("DONE")
    algo.done()
    log.close()
    pass
    
def run_algo_docker():
    """
        Runs an algorithm inside a docker container
    """
    
    cmd = ""
    docker_tag = "df-benchmarks-pandas"
    
    mem_limit = None
    cpu_limit = "1"
    
    client = docker.from_env()
    if mem_limit is None:
        mem_limit = psutil.virtual_memory().available

    container = client.containers.run(
        docker_tag,
        cmd,
        volumes={
            os.path.abspath('df_benchmark'):
                {'bind': '/home/app/df_benchmark', 'mode': 'ro'},
            os.path.abspath('datasets'):
                {'bind': '/home/app/datasets', 'mode': 'ro'},
            os.path.abspath('results'):
                {'bind': '/home/app/results', 'mode': 'rw'},
        },
        cpuset_cpus=cpu_limit,
        mem_limit=mem_limit,
        detach=True)
        
    print("CREATED CONTAINER")
    
    
    def stream_logs():
        for line in container.logs(stream=True):
            print(colors.color(line.decode().rstrip(), fg='blue'))

    t = threading.Thread(target=stream_logs, daemon=True)
    t.start()
    
    
    try:
        exit_code = container.wait(timeout=2000)

        # Exit if exit code
        try:
            exit_code = exit_code.StatusCode
        except AttributeError:
            pass
        if exit_code not in [0, None]:
            print(colors.color(container.logs().decode(), fg='red'))
            print('Child process for container %s raised exception %d' % (container.short_id, exit_code))
    except:
        print('Container.wait for container %s failed with exception' % container.short_id)
        traceback.print_exc()
    finally:
        container.remove(force=True)