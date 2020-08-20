from pensionpro.api import API as PensionProAPI
from dotenv import load_dotenv
import json, os

load_dotenv()
pensionpro = PensionProAPI(os.getenv('USERNAME'), os.getenv('API_KEY'))

with open('tests/test_data/plan_contact_role.json') as json_file:
    test_plan_contact_role = json.load(json_file)

def test_get_plan_contact_role():
    plan_contact_role = pensionpro.plan_contact_roles.get_plan_contact_role(1577995)
    assert plan_contact_role == test_plan_contact_role

def test_list_plan_contact_roles():
    plan_contact_roles = pensionpro.plan_contact_roles.list_plan_contact_roles(filter_string="RoleTypeId eq 453669")
    for role in plan_contact_roles:
        assert role["RoleTypeId"] == 453669