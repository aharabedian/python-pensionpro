import requests
from models import Contact, Plan, PlanContactRole

class ContactAPI(object):
    def __init__(self, api):
        self._api = api
    
    def get_contact(self, contact_id):
        """Fetches the contact for the given contact ID"""
        url = f'contacts/{contact_id}'
        contact = self._api._get(url)
        return Contact(**contact)

class PlanAPI(object):
    def __init__(self, api):
        self._api = api

    def get_plan(self, plan_id):
        """Fetches the plan for the given plan ID"""
        url = f'plans/{plan_id}'
        plan = self._api._get(url)
        return Plan(**plan)

class PlanContactRoleAPI(object):
    def __init__(self, api):
        self._api = api
    
    def get_plan_contact_role(self, plan_contact_role_id):
        """Fetches the plan contact role for the given plan contact role ID
            NOTE: A PlanContactRole is the association between a plan and a contact. This is NOT the role type!
        """
        url = f'plancontactroles/{plan_contact_role_id}'
        plan_contact_role = self._api._get(url)
        return PlanContactRole(**plan_contact_role)

    def list_plan_contact_roles(self, search_filter=''):
        """Returns a list of all plan contact roles that match the filter"""
        url = f'plancontactroles?$filter=' + search_filter
        response = self._api._get(url)

        plan_contact_roles = []

        for plan_contact_role in response['Values']:
            plan_contact_roles.append(plan_contact_role)
        return plan_contact_roles

class API(object):
    def __init__(self, username, api_key):
        """Creates a wrapper to perform API actions.

        Arguments:
            username: PensionPro username
            api_key: API Key
        """

        self._session = requests.Session()
        self._session.headers = {'accept': 'application/json', 'username': username, 'apikey': api_key}
        self._api_prefix = 'https://api.pensionpro.com/v1/'

        self.contacts = ContactAPI(self)
        self.plans = PlanAPI(self)
        self.plan_contact_roles = PlanContactRoleAPI(self)

    def _get(self, url, params={}):
        """Wrapper around request.get() to use API prefix. Returns the JSON response."""
        response = self._session.get(self._api_prefix + url)
        # print(self._session.headers)
        # print(response)
        # print(response.headers)
        print(response.url)
        return response.json()