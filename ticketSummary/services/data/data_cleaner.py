import re


html_regex = re.compile('<.*?>')

filtered_conversation = []


def data_cleaner(conversation):
    for message in conversation:
        filtered_message = re.sub(html_regex, '', message)
        if filtered_message:
            filtered_conversation.append(filtered_message)

    cadena = ' '.join(filtered_conversation)
    return cadena
