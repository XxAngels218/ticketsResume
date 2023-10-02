import json

from ticketSummary.services.api.api_consumer import get_access_token, get_ticket_comments


def make_data_list(ticket_id: int):
    data_list = get_ticket_comments(ticket_id, get_access_token())
    json_str = json.dumps(data_list)
    data = json.loads(json_str)

    content_list = [item["content"] for item in data]
    return content_list
