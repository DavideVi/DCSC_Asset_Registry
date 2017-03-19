from behave import *
import requests, os

ENDPOINT = os.environ['ASSET_REG_ENDPOINT']

@then('then the relevant tags should be extracted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then then the relevant tags should be extracted')
