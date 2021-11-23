from df_benchmark.run import run_algo_locally, run_algo_docker, load_algorithms, load_datasets
import argparse

if __name__ == "__main__":
    #Load available algorithms
    algorithms = load_algorithms()
    
    #Load available datasets
    datasets = load_datasets()
    
    #Set up argument parser
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--algorithm',
        choices=algorithms.keys(),
        help='Algorithm name',
        required=True
    )
    parser.add_argument(
        '--dataset',
        choices=datasets.keys(),
        help='Dataset name',
        required=True
    )
    parser.add_argument(
        '--locally',
        help='Runs the algorithm locally instead of on docker',
        default=False,
        action="store_true"
    )
    parser.add_argument(
        '--mem-limit',
        help='Memory limit for docker container (default maximum available memory)',
        default=None
    )
    parser.add_argument(
        '--cpu-limit',
        help='CPU limit for docker container (number of CPUs)',
        default=1,
        type=int
    )
    args = parser.parse_args()
    
    
    #If locally is set to true the algorithm will run locally
    if args.locally:
        run_algo_locally(args.algorithm, args.dataset)
    else:
        run_algo_docker(args.algorithm, args.dataset, args.cpu_limit, args.mem_limit)