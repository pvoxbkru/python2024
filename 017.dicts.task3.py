from pprint import pprint

device1 = {
    "hostname": "r1.abcd.net",
    "ip": "192.168.1.1",
    "username": "cisco",
    "password": "secret",
    "platform": "cisco_ios",
    "enable": True,
}

device2 = dict(
    hostname="sw1.abcd.net",
    ip="192.168.1.2",
    username="admin",
    password="secret",
    platform="huawei_vrp",
    enable=False,
)

devices_list = [device1, device2]
devices_list.append(
    {
        "hostname": "wlc.abcd.net",
        "ip": "192.168.1.3",
        "username": "wlc_admin",
        "password": "password",
        "enable": False,
    }
)

dev0 = {
    devices_list[0]["hostname"]: devices_list[0]
}
dev1 = {
    devices_list[1]["hostname"]: devices_list[1]
}
dev2 = {
    devices_list[2]["hostname"]: devices_list[2]
}
devices_dict = {**dev0, **dev1, **dev2}

pprint(devices_dict)

