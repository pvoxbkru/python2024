
# display lldp neighbor brief
lldp_output = """
GE1/0/1          br1.hq            GE0/0/5             107
GE1/0/2          br2.hq            GE0/0/5             92
GE1/0/3          sw1.hq            GE1/0/47            98
XGE1/0/1         sw2.hq            GE1/0/51            93
GE2/0/2          br2.hq            GE0/0/6             112
GE2/0/3          sw12.hq           GE1/0/48            98
XGE2/0/1         sw2.hq            GE1/0/52            93
""".strip()

# display interface description
description_output = """
GigabitEthernet1/0/1        up      up       br1.hq.net.ru
GigabitEthernet1/0/2        up      up       br2.hq.net.ru
GigabitEthernet1/0/3        up      up       sw1.hq.net.ru
GigabitEthernet2/0/1        up      up       br1.hq.net.ru
GigabitEthernet2/0/2        up      up       br2.hq.net.ru
GigabitEthernet2/0/3        up      up       sw1.hq.net.ru
XGigabitEthernet1/0/1       up      up       sw2.hq.net.ru
XGigabitEthernet2/0/1       up      up       sw2.hq.net.ru
""".strip()

lldp_dict = dict()
interface_dict = dict()

for lldp_str in lldp_output.splitlines():
    lldp_list = lldp_str.split()
    lldp_dict[lldp_list[0]] = lldp_list[1]


for interf_str in description_output.splitlines():
    interf_list = interf_str.split()
    interf_name = interf_list[0]
    intf_name_key = ""
    if interf_name.startswith("GigabitEthernet"):
        intf_name_key += "GE" + interf_name[len("GigabitEthernet"):]
    elif interf_name.startswith("XGigabitEthernet"):
        intf_name_key += "XGE" + interf_name[len("XGigabitEthernet"):]
    interface_dict[intf_name_key] = interf_list[3]

for lldp_key in lldp_dict.keys():
    if  lldp_dict[lldp_key] not in interface_dict[lldp_key]:
        print(f" {lldp_key} {lldp_dict[lldp_key]} != {interface_dict[lldp_key]}")