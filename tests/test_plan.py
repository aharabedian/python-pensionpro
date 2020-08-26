from pensionpro.api import API as PensionProAPI
from dotenv import load_dotenv
import json, os

load_dotenv()
pensionpro = PensionProAPI(os.getenv('USERNAME'), os.getenv('API_KEY'))

with open('tests/test_data/plan.json') as json_file:
    test_plan = json.load(json_file)

def test_get_plan():
    plan = pensionpro.plans.get_plan(309388)
    assert plan == test_plan

def test_list_plans():
    plans = pensionpro.plans.list_plans(top=100)
    assert len(plans) == 350
