from pensionpro.api import API as PensionProAPI
import json

username = 'aharabedian@maxusplans.com35644'
api_key = '3TEXEP7JxsrZwhZNQU4z350Z'

pensionpro = PensionProAPI(username, api_key)

with open('test_data/plan.json') as json_file:
    test_plan = json.load(json_file)

def test_get_plan():
    plan = pensionpro.plans.get_plan(309388)
    assert plan.__dict__ == test_plan
