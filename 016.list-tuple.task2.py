intf_list = ["gi0/1"]

intf_list.append("gi0/2")
list_left = ["gi0/0"]
list_res = list_left + intf_list
intf_list = list_res
print(intf_list)