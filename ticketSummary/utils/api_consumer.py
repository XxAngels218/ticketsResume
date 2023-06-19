from dataclasses import dataclass
import json
import requests


@dataclass
class Credentials:
    REFRESH_TOKEN: str = '1000.4b9efeaf45c6f8e72e7f3ad37298f538.01223c250d20846126ef20f29b1cfb52'
    CLIENT_ID: str = '1000.BTPKXDNMS6ECRX6OGBSVPSBSWFJPWO'
    CLIENT_SECRET: str = '6c3ecd8cbb1647ce6b8ce84391de40e8b50d27e61a'
    GRANT_TYPE: str = 'refresh_token'


def get_access_token():
    AUTH_URL = 'https://accounts.zoho.com/oauth/v2/token?refresh_token={}&client_id={}&client_secret={}&grant_type={}'.format(
        Credentials.REFRESH_TOKEN,
        Credentials.CLIENT_ID,
        Credentials.CLIENT_SECRET,
        Credentials.GRANT_TYPE,
    )
    response = requests.post(AUTH_URL)
    return response.json()['access_token']


def get_ticket_comments(ticket_id, access_token):
    # construir la URL de la API con el ID de ticket proporcionado
    url = f'https://desk.zoho.com/api/v1/tickets/{ticket_id}/comments'

    # construir el encabezado de autorización con el token de acceso
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # realizar la solicitud GET a la API
    response = requests.get(url, headers=headers)

    # verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # extraer los comentarios del cuerpo de la respuesta JSON
        comments = response.json().get('data')
        return comments
    else:
        # en caso de que la solicitud no sea exitosa, lanzar una excepción con el mensaje de error
        raise Exception(
            f'Error getting feedback for ticket {ticket_id}: {response.json().get("message")}')


def get_zoho_departments(access_token):
    """
    Función que hace una solicitud GET al endpoint de Zoho Desk para obtener los departamentos
    que están habilitados.
    Retorna la respuesta de la solicitud como un objeto JSON.
    """
    url = 'https://desk.zoho.com/api/v1/departments?isEnabled=true'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def make_data_list(ticket_id):
    # Tu cadena JSON
    lista = get_ticket_comments(ticket_id, get_access_token())
    json_str = json.dumps(lista)
    # Convertir la cadena JSON a una lista de Python
    data = json.loads(json_str)

    # Crear una lista con solo los valores de la clave "content"
    content_list = [item["content"] for item in data]
    return content_list


def get_tickets_byDeparment(access_token, department_id):
    # department_id = 644447000000894108
    url = f'https://desk.zoho.com/api/v1/tickets?departmentId={department_id}&include=contacts,assignee,departments,team,isRead&limit=100&sortBy=createdTime'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
