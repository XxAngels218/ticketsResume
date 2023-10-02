import requests


class ZohoDeskAPI:
    def __init__(self, Credentials):
        self.base_url = 'https://desk.zoho.com/api/v1'
        self.credentials = Credentials

    def request_tickets_comments(self, ticket_id, access_token):
        url = f'{self.base_url}/tickets/{ticket_id}/comments'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        return requests.get(url, headers=headers)

    def request_zoho_departments(self, access_token):
        url = f'{self.base_url}/departments?isEnabled=true'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        return requests.get(url, headers=headers)

    def request_tickets_by_department(self, department_id, access_token):
        url = f'{self.base_url}/tickets?departmentId={department_id}&include=contacts,assignee,departments,team,isRead&limit=100&sortBy=createdTime'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        return requests.get(url, headers=headers)

    def get_auth_url(self):
        return 'https://accounts.zoho.com/oauth/v2/token?refresh_token={}&client_id={}&client_secret={}&grant_type={}'.format(
            self.credentials.REFRESH_TOKEN,
            self.credentials.CLIENT_ID,
            self.credentials.CLIENT_SECRET,
            self.credentials.GRANT_TYPE,
        )
