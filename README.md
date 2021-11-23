# Dataframes benchmark
The aim of this benchmark is to compare several frameworks who manage DataFrames on common operations of data preparation.

## Install the benchmark
1. Clone this github repository on your machine;
2. Run `pip install -r requirements.txt`;
3. Run `python install.py` to build all the algorithms inside Docker containers\*.

\***Note**: you will need Docker installed on your machine. If you want to run the algorithms locally, avoid this step.

## Run an algorithm
The command `python run_algorithm.py --algorithm <algorithm_name> --dataset <dataset_name>` will run an algorithm on the specified dataset.
By default an algorithm running inside its Docker container, if you want to run it locally add the parameter `--locally`.

The results of a run are stored in `results/<dataset_name>/<algorithm_name>.csv`.

*run_algorithm.py* takes as input the following parameters:
* --algorithm <algorithm_name>, mandatory, the name of the algorithm to run.
* --dataset <dataset_name>, mandatory, the dataset on which run the algorithm.
* --locally, optional, if set the algorithm will run locally, otherwise it will run inside its Docker container.
* --cpu_limit <cpu_number>, optional, maximum number of CPUs that the Docker container can use.
* --mem_limit <memory_limit>, optional, maximum memory that the Docker container can use.


## Add a new dataset
1. Create a new folder named as the dataset name inside the `dataset` folder;
2. Place the new dataset file inside your folder;
3. Copy the file `dataset/tests_template.json` inside your folder renaming it as `<your_dataset_name>_template.json` and edit it;
4. Edit the file `dataset/datasets.json` by adding the new dataset.

## Add a new algorithm
1. Create a docker file for your algorithm named `Dockerfile.your_algo` inside the `install` folder. It must contain all the instructions needed to install the required libraries (see as example `Dockerfile.pandas`);
2. Create a python class named `your_algo.py` inside the folder `df_benchmark/algorithms`. The class must extend and implement all the methods of the base class contained in `df_benchmark/algorithms/base.py`;
3. Add your algorithm definition in `df_benchmark/algorithms/algorithms.json` by using the following pattern
```
{
   "name": "algorithm_name",
   "module": "df_benchmark.algorithms.algorithm_name",
   "constructor": "className",
   "constructor_args": []
}
```
* name: the name of your algorithm.
* module: the name of the module which contains your class
* constructor: name name of your class
* constructor_args: arguments that have to be passed to the constructor when the class is instantiated
