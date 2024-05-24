
devices = {
    "rt3": {
        "nb_id": 32,
        "ip": "3.3.3.3",
    },
    "rt1": {
        "nb_id": 908,
        "ip": "1.1.1.1",
    },
    "sw2": {
        "nb_id": 5233,
        "ip": "2.2.2.2",
    },
}


nb_id_lambda = lambda item: item[1]['nb_id']

out = dict(sorted(devices.items(), key=nb_id_lambda))
for k, v in out.items():
    print(f"{k}:\t{v}")
