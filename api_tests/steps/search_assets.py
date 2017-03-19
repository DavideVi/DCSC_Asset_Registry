from behave import *
import requests, os

ENDPOINT = os.environ['ASSET_REG_ENDPOINT']

@given(u'assets and their tags are present in the database')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given assets and their tags are present in the database')

@given(u'a set of tags that match the all the tags of a target asset')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a set of tags that match the all the tags of a target asset')

@when(u'we search for tags')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we search for tags')

@then(u'the target asset should be the first result')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the target asset should be the first result')

@given(u'a set of tags that match an asset more than all the others')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a set of tags that match an asset more than all the others')

@given(u'a set of tags that does not match any of the tags of a target asset')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a set of tags that does not match any of the tags of a target asset')

@then(u'the target asset should not be in the search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the target asset should not be in the search results')
