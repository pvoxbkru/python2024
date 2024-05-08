line = "switchport trunk allowed vlan 100,200,300-500,600"

vlans_str_punctuation = line.split()[-1]

vlans_list_int = tuple()
for vlan_str in vlans_str_punctuation.split(","):
    if "-" in vlan_str:
        start_vlan = vlan_str.split("-")[0]
        end_vlan = vlan_str.split("-")[1]
        vlans_list_int += tuple(vlan for vlan in range(int(start_vlan), int(end_vlan) + 1))
    else:
        vlans_list_int += (int(vlan_str),)

for vlan in int("400"), int("800"):
    print(f"vlan {vlan} {'входит' if vlan in vlans_list_int else 'не входит'} в список разрешенных на trunk'е vlan")

