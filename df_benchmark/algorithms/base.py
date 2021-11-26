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
        
    def read_json(self, path, **kwargs):
        """
        Read a json file
        """
        pass
    
    def read_csv(self, path, **kwargs):
        """
        Read a csv file
        """
        pass
        
    def read_xml(self, path, **kwargs):
        """
        Read a xml file
        """
        pass
        
    def read_excel(self, path, **kwargs):
        """
        Read an excel file
        """
        pass
        
    def read_parquet(self, path, **kwargs):
        """
        Read a parquet file
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
        pass
        
    def locate_outliers(self, column, lower_quantile=0.1, upper_quantile=0.99):
        """
        Returns the rows of the dataframe that have values
        in the provided column lower or higher than the values
        of the lower/upper quantile.
        """
        pass
        
    def get_columns_types(self):
        """
        Returns a dictionary with column types
        """
        pass
        
    def cast_columns_types(self, dtypes):
        """
        Cast the data types of the provided columns 
        to the provided new data types.
        dtypes is a dictionary that provide for each
        column to cast the new data type.
        """
        pass
        
    def get_stats(self):
        """
        Returns dataframe statistics.
        Only for numeric columns.
        Min value, max value, average value, standard deviation, and standard quantiles.
        """
        pass
        
    def find_mismatched_dtypes(self):
        """
        Returns, if exists, a list of columns with mismatched data types.
        For example, a column with string dtypes that contains only integer values.
        For every columns the list contain an object with three keys:
         - Col: name of the column
         - current_dtype: current data type
         - suggested_dtype: suggested data type
        """
        pass
        
    def check_allowed_char(self, column, pattern):
        """
        Return true if all the values of the provided column
        follow the provided pattern.
        For example, if the pattern [a-z] is provided the string
        'ciao' will return true, the string 'ciao123' will return false.
        """
        pass
        
    def drop_duplicates(self):
        """
        Drop duplicate rows.
        """
        pass
        
    def change_date_time_format(self, column, str_date_time_format):
        """
        Change the date/time format of the provided column
        according to the provided formatting string.
        column datatype must be datetime
        An example of str_date_time_format is '%m/%d/%Y'
        """
        pass
        
    def set_header_case(self, case):
        """
        Put dataframe headers in the provided case
        Supported cases: "lower", "upper", "title", "capitalize", "swapcase"
        (see definitions in pandas documentation)
        """
        pass

    def set_content_case(self, columns, case):
        """
        Put dataframe content in the provided case
        Supported cases: "lower", "upper", "title", "capitalize", "swapcase"
        (see definitions in pandas documentation)
        Columns is a list of two column names; empty list for the whole dataframe
        """
        pass

    def duplicate_columns(self, columns):
        """
        Duplicate the provided columns (add to the dataframe with "_duplicate" suffix)
        Columns is a list of column names
        """
        pass

    def pivot(self, index, columns, values, aggfunc):
        """
        Define the lists of columns to be used as index, columns and values respectively,
        and the dictionary to aggregate ("sum", "mean", "count") the values for each column: {"col1": "sum"}
        (see pivot_table in pandas documentation)
        """
        pass

    def unpivot(self, columns, var_name, val_name):
        """
        Define the list of columns to be used as values for the variable column,
        the name for variable columns and the one for value column_name
        """
        pass

    def delete_empty_rows(self, columns):
        """
        Delete the rows with null values for all provided Columns
        Columns is a list of column names
        """
        pass

    def split(self, column, sep, splits, col_names):
        """
        Split the provided column into splits + 1 columns named after col_names
        using the provided sep string as separator
        Col_names is a list of column names
        """
        pass

    def strip(self, columns, chars):
        """
        Remove the characters appearing in chars at the beginning/end of the provided columns
        Columns is a list of column names
        """
        pass

    def remove_diacritics(self, columns):
        """
        Remove diacritics from the provided columns
        Columns is a list of column names
        """
        pass
        
    def set_index(self, column):
        """
        Set the provided column as index
        """
        pass
        
        
    def change_num_format(self, formats):
        """
        Round one ore more columns to a variable number of decimal places.
        formats is a dictionary with the column names as key and the number of decimal places as value.
        """
        pass
        
    def calc_column(self, col_name, f):
        """
        Calculate the new column col_name by applying
        the function f
        """
        pass
        
    def join(self, other, left_on=None, right_on=None, how='inner', **kwargs):
        """
        Joins current dataframe (left) with a new one (right).
        left_on/right_on are the keys on which perform the equijoin
        how is the type of join
        **kwargs: additional parameters
        
        The result is stored in the current dataframe.
        """
        pass
        
    def groupby(self, columns, f):
        """
        Aggregate the dataframe by the provided columns
        then applied the function f on every group
        """
        pass
        
    def categorical_encoding(self, columns):
        """
        See label encoding / ordinal encoding by sklearn
        Convert the categorical values in these columns into numerical values
        Columns is a list of column names
        """
        pass

    def sample_rows(self, frac, num):
        """
        Return a sample of the rows of the dataframe
        Frac is a boolean:
        - if true, num is the percentage of rows to be returned
        - if false, num is the exact number of rows to be returned
        """
        pass

    def append(self, other, ignore_index):
        """
        Append the rows of another dataframe (other) at the end of the provided dataframe
        All columns are kept, eventually filled by nan
        Ignore index is a boolean: if true, reset row indices
        """
        pass

    def replace(self, columns, to_replace, value, regex):
        """
        Replace all occurrencies of to_replace (numeric, string, regex, list, dict) in the provided columns using the provided value
        Regex is a boolean: if true, to_replace is interpreted as a regex
        Columns is a list of column names
        """
        pass

    def edit(self, columns, func):
        """
        Edit the values of the cells in the provided columns using the provided expression
        Columns is a list of column names
        """
        pass

    def set_value(self, index, column, value):
        """
        Set the cell identified by index and column to the provided value
        """
        pass

    def min_max_scaling(self, columns, min, max):
        """
        Independently scale the values in each provided column in the range (min, max)
        Columns is a list of column names
        """
        pass

    def round(self, columns, n):
        """
        Round the values in columns using n decimal places
        Columns is a list of column names
        """
        pass
