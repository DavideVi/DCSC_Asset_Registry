from behave import *
import requests

ENDPOINT = "http://52.56.141.168/api"

@given('we have valid information regarding the asset')
def step_impl(context):
    context.payload = {
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
    context.response = requests.post(ENDPOINT + "/asset/add", data=context.payload)

@then('the request should succeed')
def step_impl(context):
    assert context.response.status_code is 200

@given('we have asset information that is missing mandatory data')
def step_impl(context):
        context.payload = {
            "technologies": [
                "mongo",
                "perl",
                "bash"
                ],
            "wiki_link": "http://wiki.com/project"
        }

@then('the request should return Bad Request')
def step_impl(context):
    assert context.response.status_code is 400
