import psutil

class BaseDfBench(object):
    def done(self):
        """
        Called when the execution of the algorithm is done
        """
        pass

    def get_memory_usage(self):
        """
        Return the current memory usage of this algorithm instance
        (in kilobytes), or None if this information is not available.
        """
        # return in kB for backwards compatibility
        return psutil.Process().memory_info().rss / 1024

    def load_dataset(self, path, format, **kwargs):
        """
        Load the provided dataframe
        """
        pass

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        Columns is a list of column names
        """
        pass

    def get_columns(self):
        """
        Return a list containing the names of the columns in the dataframe
        """
        pass

    def is_unique(self, column):
        """
        Check the uniqueness of all values contained in the provided column_name
        """
        pass

    def delete_columns(self, columns):
        """
        Delete the provided columns
        Columns is a list of column names
        """
        pass

    def rename_columns(self, columns):
        """
        Rename the provided columns using the provided names
        Columns is a dictionary: {"column_name": "new_name"}
        """
        pass

    def merge_columns(self, columns, separator, name):
        """
        Create a new column with the provided name combining the two provided columns using the provided separator
        Columns is a list of two column names; separator and name are strings
        """
        pass

    def fill_nan(self, value):
        """
        Fill nan values in the dataframe with the provided value
        """
        pass

    def one_hot_encoding(self, columns):
        """
        Performs one-hot encoding of the provided columns
        Columns is a list of column names
        """
        pass
        
    def locate_null_values(self, column):
        """
        Returns the rows of the dataframe which contains
        null value in the provided column.
        """
        pass
    
    def search_by_pattern(self, column, pattern):
        """
        Returns the rows of the dataframe which
        match with the provided pattern
        on the provided column.
        Pattern could be a regular expression.
        """
        
    def locate_outliers(self, column, lower_quantile=0.1, upper_quantile=0.99):
        """
        Returns the rows of the dataframe that have values
        in the provided column lower or higher than the values
        of the lower/upper quantile.
        """
        pass