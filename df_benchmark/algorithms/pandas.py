from df_benchmark.algorithms.base import BaseDfBench
import pandas as pd

class pandasBench(BaseDfBench):
    def __init__(self):
        pass

    def load_dataset(self, path, format, **kwargs):
        """
        Load the provided dataframe
        """
        if format == "csv":
            self.df = pd.read_csv(path, **kwargs)
        elif format == "json":
            self.df = pd.read_csv(path, **kwargs)
        pass

    def delete_columns(self, columns):
        """
        Delete the specified columns
        """
        return self.df.drop(columns=columns)

    def fill_nan(self, value):
        """
        Fill nan values in the dataframe with the provided value
        """
        return self.df.fillna(value)
        pass

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        """
        return self.df.sort_values(columns, ascending=ascending)
        pass
