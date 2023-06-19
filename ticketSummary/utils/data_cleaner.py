import re


# Expresión regular para filtrar contenido HTML
html_regex = re.compile('<.*?>')

# Lista para almacenar el texto legible
filtered_conversation = []


def data_cleaner(conversation):
    # Iterar a través de la lista de conversación y filtrar el contenido HTML
    for message in conversation:
        filtered_message = re.sub(html_regex, '', message)
        if filtered_message:
            filtered_conversation.append(filtered_message)

    cadena = ' '.join(filtered_conversation)
    return cadena
