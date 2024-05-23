from collections import namedtuple


config = """
spanning-tree mode rapid-pvst
spanning-tree logging
spanning-tree extend system-id
spanning-tree pathcost method long
!
lldp run
!
interface FastEthernet0/1
 switchport access vlan 10
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/2
 switchport access vlan 11
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/3
 switchport access vlan 51
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface FastEthernet0/4
 switchport mode access
 spanning-tree portfast edge
 spanning-tree bpduguard enable
!
interface GigabitEthernet0/1
 description mgmt1.core - FastEthernet0/32
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40,50-70,80,90
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/2
 description mgmt2.core - FastEthernet0/32
 switchport mode trunk
 mls qos trust cos
 ip dhcp snooping trust
!
interface GigabitEthernet0/3
  description mgmt3.core - FastEthernet0/32
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30,40,50-70,80,90
  switchport trunk allowed vlan add 150,151
  mls qos trust cos
  ip dhcp snooping trust
!
interface GigabitEthernet0/4
 description mgmt4.core - FastEthernet0/32
 ip address 1.2.3.4 255.255.255.0
!
line vty 0 4
 password cisco
!
"""


def parse_config(config):
    Config = namedtuple("Config", ("root_command", "sub_command"))
    result = {}
    lines = config.splitlines()

    current_root_command = ""
    current_sub_command = []
    for line in lines:
        if line:
            if line.startswith("exit") or line.startswith("building"):
                continue
            if current_root_command and line.startswith(" "):
                current_sub_command.append(line.strip())
            elif line[0].isalpha():
                current_sub_command = []
                current_root_command = line.strip()
            else:
                continue
            result[current_root_command] = Config(
                root_command=current_root_command,
                sub_command=current_sub_command,
            )
    return result


config_dict = parse_config(config)
for block_name, block_value in config_dict.values():
    print(f"{block_name}")
    for v in block_value:
        print(f"\t{v}")
    print("!")
