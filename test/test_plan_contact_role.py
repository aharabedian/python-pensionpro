from pensionpro.api import API as PensionProAPI
import json

username = 'aharabedian@maxusplans.com35644'
api_key = '3TEXEP7JxsrZwhZNQU4z350Z'

pensionpro = PensionProAPI(username, api_key)

with open('test_data/plan_contact_role.json') as json_file:
    test_plan_contact_role = json.load(json_file)

def test_get_plan_contact_role():
    plan_contact_role = pensionpro.plan_contact_roles.get_plan_contact_role(1577995)
    assert plan_contact_role.__dict__ == test_plan_contact_role
