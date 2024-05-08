from pprint import pprint

SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

hostnames = ["rt1", "rt2", "sw1", "sw2"]

devices = {}
for hostname in hostnames:
    scrapli_params = SCRAPLI_TEMPLATE | {"hostname": hostname}
    devices[hostname] = scrapli_params
pprint(devices)
