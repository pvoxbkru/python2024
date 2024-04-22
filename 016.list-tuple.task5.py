from collections import namedtuple
from pprint import pprint

InterfaceStatus = namedtuple(
    typename="InterfaceStatus",
    field_names=[
        "name",
        "ip",
        "status",
    ],
)

output = """
Interface             IP-Address      OK?    Method Status      Protocol
GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
TenGigabitEthernet2/1 unassigned      YES    unset  up          up
Te36/45               unassigned      YES    unset  down        down
""".strip()


list_str = output.split("\n")
# int1 = list_str[1].split()
# int2 = list_str[2].split()
# int3 = list_str[3].split()
# int4 = list_str[4].split()
list_int = [list_str[i].split() for i in range(1, len(list_str))]

# n1 = InterfaceStatus(int1[0], int1[1], int1[4])
# n2 = InterfaceStatus(int2[0], int2[1], int2[4])
# n3 = InterfaceStatus(int3[0], int3[1], int3[4])
# n4 = InterfaceStatus(int4[0], int4[1], int4[4])
intf_brief = [ InterfaceStatus(i[0], i[1], i[4]) for i in list_int ]

# intf_brief = list()
# intf_brief.append(n1)
# intf_brief.append(n2)
# intf_brief.append(n3)
# intf_brief.append(n4)
pprint(intf_brief)
