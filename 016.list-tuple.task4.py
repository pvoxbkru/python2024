output = "switchport trunk allowed vlan 2,101,104"

out_vlans = output.split()[-1]
vlans_str = out_vlans.split(",")
vlans = [int(s) for s in vlans_str]
print(vlans)
