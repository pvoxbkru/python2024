access = """
interface {if_name}
   switchport mode access
   switchport access vlan {vlan}
!
""".strip()

trunk = """
interface {if_name}
   switchport mode trunk
   switchport trunk allowed vlan {vlan}
!
""".strip()

intf1 = {
    "if_name": "gi0/1",
    "vlan": 102,
    "mode": "access",
}

intf2 = {
    "if_name": "gi0/2",
    "vlan": 103,
    "mode": "trunk",
}

intf_config1 = access.format(if_name=intf1["if_name"], vlan=intf1["vlan"])
intf_config2 = trunk.format(if_name=intf2["if_name"], vlan=intf2["vlan"])

print(intf_config1)
print(intf_config2)
