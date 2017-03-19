from behave import *
import requests, os

ENDPOINT = os.environ['ASSET_REG_ENDPOINT']

@given(u'there is an asset in the registry')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given there is an asset in the registry')

@when(u'the user requests the assets')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user requests the assets')

@then(u'the assets should be returned to the user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the assets should be returned to the user')
