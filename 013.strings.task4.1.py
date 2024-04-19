from textwrap import dedent

template = dedent(
"""
#
bridge-domain {bd_id}
 vlan {bd_id} access-port interface {intf_start} to {intf_end}
 vxlan vni {bd_id}
 #
 evpn
  route-distinguisher {rid}:{bd_id}
  vpn-target {bgp_as}:{bd_id} export-extcommunity
  vpn-target {bgp_as}:{bd_id} import-extcommunity
 arp broadcast-suppress enable
#
"""
)

for id in "555", "2541", "84":
    config = template.format(
        bd_id = "1" + f"{id:0>4}",
        intf_start = "10GE1/0/1",
        intf_end = "10GE1/0/48",
        rid = "192.168.43.34",
        bgp_as = "64512",
    )
    print(config)
