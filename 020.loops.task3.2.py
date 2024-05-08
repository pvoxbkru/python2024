from pprint import pprint 

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

hostnames = ["rt1", "rt2", "sw1", "sw2"]

devices = { hostname: SCRAPLI_TEMPLATE | {"hostname": hostname} for hostname in hostnames}

pprint(devices)