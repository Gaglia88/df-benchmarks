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
        
    def fill_nan(self, value):
        """
        Fill nan values in the dataframe with the provided value
        """
        pass
    
    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns.
        """
        pass