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
            self.df = self.read_csv(path, **kwargs)
        elif format == "json":
            self.df = self.read_json(path, **kwargs)
        elif format == "xml":
            self.df = self.read_json(path, **kwargs)
        elif format == "excel":
            self.df = self.read_json(path, **kwargs)
        elif format == "parquet":
            self.df = self.read_json(path, **kwargs)
        pass
        
    def read_json(self, path, **kwargs):
        """
        Read a json file
        """
        self.df = pd.read_json(path, **kwargs)
        pass
    
    def read_csv(self, path, **kwargs):
        """
        Read a csv file
        """
        self.df = pd.read_csv(path, **kwargs)
        pass
        
    def read_xml(self, path, **kwargs):
        """
        Read a xml file
        """
        self.df = pd.read_xml(path, **kwargs)
        pass
        
    def read_excel(self, path, **kwargs):
        """
        Read an excel file
        """
        self.df = pd.read_excel(path, **kwargs)
        pass
        
    def read_parquet(self, path, **kwargs):
        """
        Read a parquet file
        """
        self.df = pd.read_parquet(path, **kwargs)
        pass

    def sort(self, columns, ascending=True):
        """
        Sort the dataframe by the provided columns
        Columns is a list of column names
        """
        self.df = self.df.sort_values(columns, ascending=ascending)
        return self.df

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
        self.df = self.df.drop(columns=columns)
        return self.df

    def rename_columns(self, columns):
        """
        Rename the provided columns using the provided names
        Columns is a dictionary: {"column_name": "new_name"}
        """
        self.df = self.df.rename(columns=columns)
        return self.df

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
        self.df = self.df.fillna(value)
        return self.df

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
        self.df = self.df.astype(dtypes)
        return self.df
        
        
    def get_stats(self):
        """
        Returns dataframe statistics.
        Only for numeric columns.
        Min value, max value, average value, standard deviation, and standard quantiles.
        """
        return df.describe()
        
        
    def find_mismatched_dtypes(self):
        """
        Returns, if exists, a list of columns with mismatched data types.
        For example, a column with string dtypes that contains only integer values.
        For every columns the list contain an object with three keys:
         - Col: name of the column
         - current_dtype: current data type
         - suggested_dtype: suggested data type
        """
        current_dtypes = self.get_columns_types()
        new_dtypes = self.df.apply(pd.to_numeric, errors='ignore').dtypes.apply(lambda x: x.name).to_dict()

        out = []
        for k in current_dtypes.keys():
            if new_dtypes[k] != current_dtypes[k]:
                out.append({'col': k, 'current_dtype': current_dtypes[k], 'suggested_dtype': new_dtypes[k]})
        return out
        
    def check_allowed_char(self, column, pattern):
        """
        Return true if all the values of the provided column
        follow the provided pattern.
        For example, if the pattern [a-z] is provided the string
        'ciao' will return true, the string 'ciao123' will return false.
        """
        return self.df[column].str.contains(re.compile(pattern)).all()
        
    def drop_duplicates(self):
        """
        Drop duplicate rows.
        """
        self.df = self.df.drop_duplicates()
        return self.df
        
    def drop_by_pattern(self, column, pattern):
        """
        Delete the rows where the provided pattern
        occurs in the provided column.
        """
        matching_rows = self.search_by_pattern(column, pattern)
        self.df = self.df.drop(matching_rows.index)
        return self.df
        
    def change_date_time_format(self, column, str_date_time_format):
        """
        Change the date/time format of the provided column
        according to the provided formatting string.
        column datatype must be datetime
        An example of str_date_time_format is '%m/%d/%Y'
        """
        self.df[column] = pd.to_datetime(self.df[column].dt.strftime(str_date_time_format))
        return self.df
        
    def set_header_case(self, case):
        """
        Put dataframe headers in the provided case
        Supported cases: "lower", "upper", "title", "capitalize", "swapcase"
        (see definitions in pandas documentation)
        """
        if mode == "lower":
            self.df.columns = map(str.lower, self.df.columns)
        elif mode == "upper":
            self.df.columns = map(str.upper, self.df.columns)
        elif mode == "title":
            self.df.columns = map(str.title, self.df.columns)
        elif mode == "capitalize":
            self.df.columns = map(str.capitalize, self.df.columns)
        elif mode == "swapcase":
            self.df.columns = map(str.swapcase, self.df.columns)
        return self.df

    def set_content_case(self, columns, case):
        """
        Put dataframe content in the provided case
        Supported cases: "lower", "upper", "title", "capitalize", "swapcase"
        (see definitions in pandas documentation)
        Columns is a list of two column names; empty list for the whole dataframe
        """
        if len(columns) == 0:
            columns = list(self.df.columns.values)
        for column in columns:
            if mode == "lower":
                self.df[column] = self.df[column].str.lower()
            elif mode == "upper":
                self.df[column] = self.df[column].str.upper()
            elif mode == "title":
                self.df[column] = self.df[column].str.title()
            elif mode == "capitalize":
                self.df[column] = self.df[column].str.capitalize()
            elif mode == "swapcase":
                self.df[column] = self.df[column].str.swapcase()
        return self.df

    def duplicate_columns(self, columns):
        """
        Duplicate the provided columns (add to the dataframe with "_duplicate" suffix)
        Columns is a list of column names
        """
        for column in columns:
            self.df[column + "_duplicate"] = self.df[column]
        return self.df

    def pivot(self, index, columns, values, aggfunc):
        """
        Define the lists of columns to be used as index, columns and values respectively,
        and the dictionary to aggregate ("sum", "mean", "count") the values for each column: {"col1": "sum"}
        (see pivot_table in pandas documentation)
        """
        return pd.pivot_table(self.df, index=index, values=values, columns=columns, aggfunc=aggfunc).reset_index()

    def unpivot(self, columns, var_name, val_name):
        """
        Define the list of columns to be used as values for the variable column,
        the name for variable columns and the one for value column_name
        """
        return pd.melt(self.df, id_vars=list(set(list(self.df.columns.values)) - set(columns)), value_vars=columns, var_name=var_name, value_name=val_name)

    def delete_empty_rows(self, columns):
        """
        Delete the rows with null values for all provided Columns
        Columns is a list of column names
        """
        return self.df.dropna(subset = columns, inplace=True)

    def split(self, column, sep, splits, col_names):
        """
        Split the provided column into splits + 1 columns named after col_names
        using the provided sep string as separator
        Col_names is a list of column names
        """
        self.df[col_names] = self.df[column].str.split(sep, splits, expand=True)
        return self.df

    def strip(self, columns, chars):
        """
        Remove the characters appearing in chars at the beginning/end of the provided columns
        Columns is a list of column names
        """
        for column in columns:
            self.df[column] = self.df[column].str.strip(chars)
        return self.df

    def remove_diacritics(self, columns):
        """
        Remove diacritics from the provided columns
        Columns is a list of column names
        """
        for column in columns:
            self.df[column] = self.df[column].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        return self.df
        
    def set_index(self, column):
        """
        Set the provided column as index
        """
        self.df = self.df.set_index(column)
        return self.df
        
        
    def change_num_format(self, formats):
        """
        Round one ore more columns to a variable number of decimal places.
        formats is a dictionary with the column names as key and the number of decimal places as value.
        """
        self.df = self.df.round(formats)
        return self.df
        
        
    def calc_column(self, col_name, f):
        """
        Calculate the new column col_name by applying
        the function f
        """
        self.df[col_name] = self.df.apply(f, axis=1)
        return self.df
        
    def join(self, other, left_on=None, right_on=None, how='inner', **kwargs):
        """
        Joins current dataframe (left) with a new one (right).
        left_on/right_on are the keys on which perform the equijoin
        how is the type of join
        **kwargs: additional parameters
        
        The result is stored in the current dataframe.
        """
        self.df = self.df.merge(other, left_on=left_on, right_on=right_on, how=how, **kwargs)
        return self.df
        
    def groupby(self, columns, f):
        """
        Aggregate the dataframe by the provided columns
        then applied the function f on every group
        """
        return self.df.groupby(columns).agg(f)
        
    
    def categorical_encoding(self, columns):
        """
        Convert the categorical values in these columns into numerical values
        Columns is a list of column names
        """
        for column in columns:
            self.df[column] = self.df[column].astype('category')
            self.df[column] = self.df[column].cat.codes
        return self.df

    def sample_rows(self, frac, num):
        """
        Return a sample of the rows of the dataframe
        Frac is a boolean:
        - if true, num is the percentage of rows to be returned
        - if false, num is the exact number of rows to be returned
        """
        if frac:
            return self.df.sample(frac=num/100)
        else:
            return self.df.sample(n=num)

    def append(self, other, ignore_index):
        """
        Append the rows of another dataframe (other) at the end of the provided dataframe
        All columns are kept, eventually filled by nan
        Ignore index is a boolean: if true, reset row indices
        """
        self.df = self.df.append(other, ignore_index=ignore_index)
        return self.df

    def replace(self, columns, to_replace, value, regex):
        """
        Replace all occurrencies of to_replace (numeric, string, regex, list, dict) in the provided columns using the provided value
        Regex is a boolean: if true, to_replace is interpreted as a regex
        Columns is a list of column names
        """
        self.df[columns] = self.df[columns].replace(to_replace=to_replace, value=value, regex=regex)
        return self.df

    def edit(self, columns, func):
        """
        Edit the values of the cells in the provided columns using the provided expression
        Columns is a list of column names
        """
        self.df[columns] = self.df[columns].apply(func)
        return self.df

    def set_value(self, index, column, value):
        """
        Set the cell identified by index and column to the provided value
        """
        self.df.at[index, column] = value
        return self.df

    def min_max_scaling(self, columns):
        """
        Independently scale the values in each provided column in the range (0, 1)
        Columns is a list of column names
        """
        for column in columns:
            self.df[column] = self.df[column] - self.df[column].min()
            self.df[column] = self.df[column] / self.df[column].max()
            self.df[column] = self.df[column] * (max - min) + min
        return self.df

    def round(self, columns, n):
        """
        Round the values in columns using n decimal places
        Columns is a list of column names
        """
        self.df[columns] = self.df[columns].round(n)
        return self.df