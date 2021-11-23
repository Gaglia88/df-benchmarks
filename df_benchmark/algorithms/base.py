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

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        Columns is a list of column names
        """
        pass

    def one_hot_encoding(self, columns):
        """
        Performs one-hot-encoding of the provided columns
        Columns is a list of column names
        """
        pass
