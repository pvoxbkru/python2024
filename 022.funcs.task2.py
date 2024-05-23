interfaces = [
    "Eth0/0",
    "Gig0/4/3",
    "GE4/4",
    "Po3",
    "Ten5/4",
    "XGE4/1",
    "Eth-Trunk4",
]


def get_norm_intf_name(intf_name):
    intf_dict = {
        "Eth": "Ethernet",
        "Fa": "FastEthernet",
        "Gig": "GigabitEthernet",
        "GE": "GigabitEthernet",
        "Ten": "TenGigabitEthernet",
        "TE": "TenGigabitEthernet",
        "XGE": "TenGigabitEthernet",
    }

    def check_dict(intf_name, count_char, *args):
        for intf_key in args:
            if intf_name[:count_char] == intf_key:
                return intf_dict[intf_key] + intf_name[count_char:]
        return intf_name

    intf_norm_name = intf_name

    if intf_name[:3].isalpha() and intf_name[3].isdigit():
        intf_norm_name = check_dict(intf_name, 3, "Eth", "Gig", "Ten", "XGE")
    elif intf_name[:2].isalpha() and intf_name[2].isdigit():
        intf_norm_name = check_dict(intf_name, 2, "Fa", "GE", "TE")

    return intf_norm_name


for intf in interfaces:
    print(f"{intf} : {get_norm_intf_name(intf)}")
