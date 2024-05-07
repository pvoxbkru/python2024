mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]

uppercase_chars = ["A", "B", "C", "D", "E", "F"]

for mac in mac_list:
    if "-" in mac and any(char in mac for char in uppercase_chars):
        mac_notation = "IEEE EUI-48"
    elif "-" in mac and (
        "a" in mac or "b" in mac or "c" in mac or "d" in mac or "e" in mac or "f" in mac
    ):
        mac_notation = "IEEE EUI-48 lowercase"
    elif ":" in mac and len(mac.split(":")) == 6:
        mac_notation = "UNIX"
    elif ":" in mac and len(mac.split(":")) == 3:
        mac_notation = "cisco"
    elif "-" not in mac and ":" not in mac:
        mac_notation = "bare"
    else:
        mac_notation = "неизвестна"

    print(f"нотация {mac}: {mac_notation}")
