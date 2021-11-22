# Dataframes benchmark
The aim of this benchmark is to compare several frameworks who manage DataFrames on common operations of data preparation.

## Add a new dataset
1. Create a new folder named as the dataset name inside the `dataset` folder;
2. Place the new dataset file inside your folder;
3. Copy the file `dataset/tests_template.json` inside your folder renaming it as `<your_dataset_name>_template.json` and edit it;
4. Edit the file `dataset/datasets.json` by adding the new dataset.

## Add a new algorithm
1. Create a docker file for your algorithm named `Dockerfile.your_algo` inside the `install` folder. It must contain all the instructions needed to install the required libraries (see as example `Dockerfile.pandas`);
2. Create a python class named `your_algo.py` inside the folder `df_benchmark/algorithms`. The class must extend and implement all the methods of the base class contained in `df_benchmark/algorithms/base.py`;
3. Add your algorithm definition in `df_benchmark/algorithms/algorithms.json` by using the following patter
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