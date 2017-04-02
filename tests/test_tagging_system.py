import unittest, requests, os, json
from pymongo import MongoClient

from data_provider import DataProvider

AR_ENDPOINT = os.environ['AR_ENDPOINT']
ENDPOINT = AR_ENDPOINT + "/api/asset/"

MONGODB_URI = os.environ['MONGODB_URI']

class TestTaggingSystem(unittest.TestCase):

    '''
    Ran before every test
        Gets the database connection
        Clears the database
    '''
    def setUp(self):
        database_uri = MONGODB_URI.split('/')

        client = MongoClient('mongodb://' + database_uri[0])
        self.db = client[database_uri[1]]

        db.tags.delete_many({})
        db.assets.delete_many({})

    '''
    Checks whether author tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_author_tags(self):
        pass

    '''
    Checks whether technology tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_tech_tags(self):
        pass

    '''
    Checks whether NLP tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_nlp_tags(self):
        pass

    '''
    Checks whether tags are added to assets after being generated
    Checks for duplication
    '''
    def test_add_tagging(self):
        pass

if __name__ == '__main__':
    unittest.main()
