from behave import *
import requests

payload = {}
ENDPOINT = "http://demo/api"
response = {}

@given('we have valid information regarding the asset')
def step_impl(context):
    payload = {
        "asset_name": "",
        "asset_purpose": "",
        "author_ids": [
            "leia.solo",
            "john.smith"
            ],
        "technologies": [
            "mongo",
            "perl",
            "bash"
            ],
        "stability": 0,
        "scm_link": "http://scm.com/project.git",
        "wiki_link": "http://wiki.com/project"
    }

@when('we request to add an asset')
def step_impl(context):
    response = requests.post(ENDPOINT + "/assets/add", data=payload)

@then('the request should succeed')
def step_impl(context):
    assert response.status_code is 200
