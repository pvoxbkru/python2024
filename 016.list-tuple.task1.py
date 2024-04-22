intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]

list_a = intf_list[:2]
list_a.append("gi0/2")
list_b = intf_list[-2:]
list_a.extend(list_b)
print(list_a)
