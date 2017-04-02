import unittest, requests, os, json
from pymongo import MongoClient

from data_provider import DataProvider

AR_ENDPOINT = os.environ['AR_ENDPOINT']
ADD_ENDPOINT = AR_ENDPOINT + "/api/asset/add"

MONGODB_URI = os.environ['MONGODB_URI']
NLP_ENDPOINT = os.environ['NLP_ENDPOINT'] + "/?properties=%7B%22annotators%22%3A%20%22tokenize%2Cssplit%2Cpos%2Cner%2Cdepparse%2Copenie%22%2C%20%22openie.resolve_coref%22%3A%20%22true%22%7D"

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

        # self.db.tags.delete_many({})
        # self.db.assets.delete_many({})

    '''
    Checks whether author tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_author_tags(self):

        payload = DataProvider.get_payload("POST_asset_add.tag_payload.0.json")

        # Request is made twice to check for tag duplication
        response_one = requests.post(ADD_ENDPOINT, data=payload)
        response_two = requests.post(ADD_ENDPOINT, data=payload)

        found_count = 0

        for doc in self.db.tags.find({'type': 'author'}):
            if doc["value"] in payload["author_ids"]:
                found_count += 1

        self.assertEqual(len(payload["author_ids"]), found_count)

        # result = self.db.tags.find({'type': 'author', 'tagged': { "$in" : [response_one.json()["asset_id"]] }}).count()
        # self.assertEqual(1, result, "Tag has been generated but asset has not been tagged")

    '''
    Checks whether technology tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_tech_tags(self):

        payload = DataProvider.get_payload("POST_asset_add.tag_payload.0.json")

        # Request is made twice to check for tag duplication
        response_one = requests.post(ADD_ENDPOINT, data=payload)
        response_two = requests.post(ADD_ENDPOINT, data=payload)

        found_count = 0

        for doc in self.db.tags.find({'type': 'technology'}):
            if doc["value"] in payload["technologies"]:
                found_count += 1

        self.assertEqual(len(payload["technologies"]), found_count)

    '''
    Checks whether NLP tags are generated when we add an asset
    Checks for duplication
    '''
    def test_add_nlp_tags(self):

        payload = DataProvider.get_payload("POST_asset_add.tag_payload.0.json")

        # Request is made twice to check for tag duplication
        response_one = requests.post(ADD_ENDPOINT, data=payload)
        response_two = requests.post(ADD_ENDPOINT, data=payload)

        # Getting POS annotations
        nlp_response = requests.post(NLP_ENDPOINT, data=payload["asset_purpose"])

        tags_to_store = ["NN", "NNS","VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "JJ", "JJR", "JJS","RB", "RBR", "RBS"]
        expected_tags = []
        for sentence in nlp_response.json()["sentences"]:
            for token in sentence["tokens"]:
                if token["pos"] in tags_to_store:
                    expected_tags.append(token["lemma"])

        # Checking if tags were added
        found_count = 0
        for doc in self.db.tags.find({'type': 'NLP'}):
            if doc["value"] in expected_tags:
                found_count += 1

        self.assertEqual(len(expected_tags), found_count, "NLP tags not extracted correctly: Found " + str(found_count) + "; Expected: " + str(len(expected_tags)))


if __name__ == '__main__':
    unittest.main()
