from pprint import pprint

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

dict1 = dict(
    hostname = "sw1.abcd.net",
)
dict2 = dict(
    hostname = "sw1.abcd.net",
    transport = "telnet",
    port = "23",
)

scrapli_dict1 = SCRAPLI_TEMPLATE | dict1

scrapli_dict2 = SCRAPLI_TEMPLATE | dict2
