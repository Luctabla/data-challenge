import pandas
import config

class DataHelper:
    def __init__(self):
        self.open_file()

    def open_file(self):
        self.df = pandas.read_csv(config.SOURCE_DATA, converters={'Value': float})

    def countries_by_indicator(self, indicator, index_value):
        by_indicator = self.df[self.df[config.INDICATOR_COLUMN] == indicator]
        by_inequality = by_indicator[by_indicator[config.INEQUALITY_COLUMN] == config.TOTAL_VALUE]
        by_index_value = by_inequality[by_inequality[config.VALUE_COLUMN] > float(index_value)]

        result = by_index_value[config.COUNTRY_COLUMN]
        return result.head()

    def validate_filters(self, filter, index_value):
        try:
            float(index_value)
            if not filter in config.INDICATORS_ALLOWED:
                raise Exception
        except:
            raise Exception

