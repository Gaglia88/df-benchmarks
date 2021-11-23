import importlib
import time
import docker
import os
import json
import psutil
import colors
import threading
import traceback

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

def run_algo_locally(algorithm, dataset):
    """
        Runs an algorithm on local machine
    """
    
    #Load available algorithms
    algorithms = load_algorithms()
    
    #Load available datasets
    datasets = load_datasets()
    
    #Load the current algorithm
    algo = create_algo(algorithms[algorithm])
    
    #Create log file
    log = get_logger(dataset, algorithm)
    
    #Load the tests to perform on the dataset
    tests = load_tests(datasets[dataset]['tests'])
    
    
    
    #Execute each test on the dataset
    for test in tests:
        print("Running "+test['method'])
        if test['method'] == 'load_dataset':
            #Load the data
            mstart = algo.get_memory_usage()
            tstart = time.time()
            algo.load_dataset(datasets[dataset]['path'], datasets[dataset]['type'], **test['input'])
            t = time.time()-tstart
            m = algo.get_memory_usage()-mstart
        else:
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
    
def run_algo_docker(algorithm, dataset, cpu_limit=None, mem_limit=None):
    """
        Runs an algorithm inside a docker container
    """
    
    cmd = ['--dataset', dataset,
           '--algorithm', algorithm,
           '--locally'
          ]
          
    docker_tag = "df-benchmarks-"+algorithm
    
    if mem_limit is None:
        mem_limit = psutil.virtual_memory().available
    
    if cpu_limit is None:
        cpu_limit = "1"
    
    client = docker.from_env()
    

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
        cpuset_cpus=str(cpu_limit),
        mem_limit=mem_limit,
        detach=True)
    
    def stream_logs():
        for line in container.logs(stream=True):
            print(colors.color(line.decode().rstrip(), fg='blue'))

    t = threading.Thread(target=stream_logs, daemon=True)
    t.start()
    
    
    try:
        exit_code = container.wait(timeout=20000)

        # Exit if exit code
        try:
            exit_code = exit_code['StatusCode']
        except AttributeError:
            pass

        if exit_code not in [0, None]:
            print(colors.color(container.logs().decode(), fg='red'))
            print("Child process for container", container.short_id,  "raised exception", exit_code)
    except:
        print("Container.wait for container ", container.short_id, " failed with exception")
        traceback.print_exc()
    finally:
        container.remove(force=True)