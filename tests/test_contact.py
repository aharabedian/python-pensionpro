from pensionpro.api import API as PensionProAPI
from dotenv import load_dotenv
import json, os

load_dotenv()
pensionpro = PensionProAPI(os.getenv('USERNAME'), os.getenv('API_KEY'))

with open('tests/test_data/contact.json') as json_file:
    test_contact = json.load(json_file)

def test_get_contact():
    contact = pensionpro.contacts.get_contact(1030562)
    assert contact.__dict__ == test_contact