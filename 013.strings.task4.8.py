if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Тen4/3"

if_name1 = "Ethernet" + if_name1[-3:]
if_name2 = "GigabitEthernet{}".format(if_name2[-5:])
if_name3 = "TenGigabitEthernet{index}".format(index = if_name3[-3:])

print(if_name1)
#'Ethernet0/1'
print(if_name2)
#'GigabitEthernet1/0/2'
print(if_name3)
#'TenGigabitEthernet4/3'