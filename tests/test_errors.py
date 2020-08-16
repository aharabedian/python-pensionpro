from pensionpro.api import API as PensionProAPI
from pensionpro.errors import *
import pytest
from dotenv import load_dotenv
import json, os

load_dotenv()
pensionpro = PensionProAPI(os.getenv('USERNAME'), os.getenv('API_KEY'))
unauthorized_pensionpro = PensionProAPI('FAKE','123')

def test_bad_request():
    pass

def test_unauthorized():
    with pytest.raises(PensionProUnauthorized):
        unauthorized_pensionpro.plan_contact_roles.list_plan_contact_roles()

def test_rate_limited():
    pass

def test_not_found():
    with pytest.raises(PensionProNotFound):
        pensionpro._get('/unknown/url/bad/request')

def test_server_error():
    pass