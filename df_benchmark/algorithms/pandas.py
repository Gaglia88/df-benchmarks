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

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        Columns is a list of column names
        """
        return self.df.sort_values(columns, ascending=ascending)

    def get_columns(self):
        """
        Return the name of the columns in the dataframe
        """
        return list(self.df.columns.values)

    def is_unique(self, column):
        """
        Check the uniqueness of all values contained in the provided column_name
        """
        return self.df[column].is_unique

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

    def one_hot_encoding(self, columns):
        """
        Performs one-hot encoding of the provided columns
        Columns is a list of column names
        """
        dummies = pd.get_dummies(self.df[columns])
        return pd.concat([self.df.drop(columns=columns), dummies], axis=1)
        
        
        
    def locate_null_values(self, column):
        """
        Returns the rows of the dataframe which contains
        null value in the provided column.
        """
        return self.df[self.df[column].isna()]
    
    def search_by_pattern(self, column, pattern):
        """
        Returns the rows of the dataframe which
        match with the provided pattern
        on the provided column.
        Pattern could be a regular expression.
        """
        return self.df[self.df[column].str.contains(re.compile(pattern))]
        
    def locate_outliers(self, column, lower_quantile=0.1, upper_quantile=0.99):
        """
        Returns the rows of the dataframe that have values
        in the provided column lower or higher than the values
        of the lower/upper quantile.
        """
        q_low = self.df[column].quantile(lower_quantile)
        q_hi  = self.df[column].quantile(upper_quantile)
        return self.df[(self.df[column] < q_low) | (self.df[column] > q_hi)]
        
    def get_columns_types(self):
        """
        Returns a dictionary with column types
        """
        return self.df.dtypes.apply(lambda x: x.name).to_dict()
        
    def cast_columns_types(self, dtypes):
        """
        Cast the data types of the provided columns 
        to the provided new data types.
        dtypes is a dictionary that provide for each
        column to cast the new data type.
        """
        return self.df.astype(dtypes)
    
