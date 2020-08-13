from pensionpro.api import API as PensionProAPI
import json

username = 'aharabedian@maxusplans.com35644'
api_key = '3TEXEP7JxsrZwhZNQU4z350Z'

pensionpro = PensionProAPI(username, api_key)
contact = pensionpro.contacts.get_contact(1030562)

with open('test_data/contact.json') as json_file:
    test_contact = json.load(json_file)

def test_contact_id():
    assert contact.Id == test_contact.get('Id')

def test_all():
    assert contact.__dict__ == test_contact