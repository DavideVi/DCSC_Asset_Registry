import json

from logger import Logger
from test_blocked_exception import TestBlockedException

class DataProvider():

    @staticmethod
    def get_data(file_name):
        Logger.log_info("Loading datafile '" + file_name + "'")
        try:
            with open('./data/' + file_name) as data_file:
                return json.load(data_file)
        except Exception, e:
            Logger.log_error("Could not load datafile '" + file_name + "'")
            Logger.log_error(e)
            raise TestBlockedException
