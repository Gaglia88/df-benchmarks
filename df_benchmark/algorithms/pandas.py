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
        Columns is a list of column names
        """
        return self.df.drop(columns=columns)

    def rename_columns(self, columns):
        """
        Rename the provided columns using the provided names
        Columns is a dictionary: {"column_name": "new_name"}
        """
        return self.df.rename(columns=columns)

    def merge_columns(self, columns, separator, name):
        """
        Create a new column with the provided name combining the two provided columns using the provided separator
        Columns is a list of two column names; separator and name are strings
        """
        self.df[name] = self.df[columns[0]].astype(str) + separator + self.df[columns[1]].astype(str)
        return self.df

    def fill_nan(self, value):
        """
        Fill nan values in the dataframe with the provided value
        """
        return self.df.fillna(value)
        pass

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        Columns is a list of column names
        """
        return self.df.sort_values(columns, ascending=ascending)

    def one_hot_encoding(self, columns):
        """
        Performs one-hot-encoding of the provided columns
        Columns is a list of column names
        """
        dummies = pd.get_dummies(self.df[columns])
        return pd.concat([self.df.drop(columns=columns), dummies], axis=1)
