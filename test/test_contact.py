from pensionpro.api import API as PensionProAPI
import json

username = 'aharabedian@maxusplans.com35644'
api_key = '3TEXEP7JxsrZwhZNQU4z350Z'

pensionpro = PensionProAPI(username, api_key)

with open('test_data/contact.json') as json_file:
    test_contact = json.load(json_file)

def test_get_contact():
    contact = pensionpro.contacts.get_contact(1030562)
    assert contact.__dict__ == test_contact