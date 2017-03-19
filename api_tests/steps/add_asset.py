from behave import *
import requests, os

ENDPOINT = os.environ['ASSET_REG_ENDPOINT']
# ENDPOINT = "http://52.56.141.168/api"

@given('we have valid information regarding an asset')
def step_impl(context):
    context.payload = {
        "asset_name": "Perl Mongo Migrator",
        "asset_purpose": "This script migrates mongo databases using Perl",
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

@then('the request should succeed and return asset ID')
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
