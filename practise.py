import xmltodict
import pprint

with open("users.xml", 'r') as file:
    lines= file.read()
    data = xmltodict.parse(lines)
    for user in data['users']['user']:
        print(pprint.pformat(user['id']['#text']))