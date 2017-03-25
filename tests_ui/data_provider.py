import json

class DataProvider():

    @staticmethod
    def get_data(file_name):
        with open('./data/' + file_name) as data_file:
            return json.load(data_file)
