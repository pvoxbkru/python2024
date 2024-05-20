vlan_string = "10,20,30,31,32,33,34,35,40"

vlans = map(int, vlan_string.split(","))
result_string = ""
range_ = 0
for vlan in vlans:
    if len(result_string):
        if vlan == vlan_before + 1:
            range_ = 1
        else:
            if range_:
                result_string += "-" + str(vlan_before)
                result_string += "," + str(vlan)
                range_ = 0
            else:
                result_string += "," + str(vlan)
    else:
        result_string += str(vlan)
    vlan_before = vlan
print(result_string)