from dataclasses import dataclass
from dotenv import load_dotenv
import os
import requests
import http.client

from ticketSummary.services.api.services_api import ZohoDeskAPI
from ticketSummary.services.api.api_error import ApiError

load_dotenv()


@dataclass
class Credentials:
    REFRESH_TOKEN: str = os.getenv("REFRESH_TOKEN")
    CLIENT_ID: str = os.getenv("CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
    GRANT_TYPE: str = os.getenv("GRANT_TYPE")


api = ZohoDeskAPI(Credentials)


def get_access_token():
    response = requests.post(api.get_auth_url())
    return response.json()['access_token']


def get_ticket_comments(ticket_id: int, access_token: get_access_token) -> get_access_token:
    response = api.request_tickets_comments(ticket_id, access_token)

    if response.status_code == http.client.OK:
        return response.json().get('data')

    raise ApiError(
        f'Error getting comments for ticket {ticket_id}')


def get_zoho_departments(access_token: get_access_token) -> get_access_token:
    """
    Function that makes a GET request to the Zoho Desk endpoint to retrieve the enabled departments.
    Returns the response of the request as a JSON object.
    """
    response = api.request_zoho_departments(access_token)

    if response.status_code == http.client.OK:
        return response.json()

    raise ApiError('Error getting departments from zoho desk')


def get_tickets_by_deparment(department_id: int, access_token: get_access_token) -> get_access_token:
    response = api.request_tickets_by_department(access_token, department_id)

    if response.status_code == http.client.OK:

        return response.json()
    raise ApiError('Error getting tickets by department from zoho desk')
