address = [192, 168, 43, 54]
mask1 = [255, 255, 254, 0]
mask2 = [255, 255, 255, 240]

# network
network1 = [x & y for x, y in zip(address, mask1)]
network2 = [x & y for x, y in zip(address, mask2)]

# wildcard
wildcard1 = [255 ^ x for x in mask1]
wildcard2 = [255 ^ x for x in mask2]

# broadcast
broadcast1 = [x | y for x, y in zip(address, wildcard1)]
broadcast2 = [x | y for x, y in zip(address, wildcard2)]

# min_host_ip
min_host_ip1 = network1[0:3]
min_host_ip1.append(network1[-1] + 1)
min_host_ip2 = network2[0:3]
min_host_ip2.append(network2[-1] + 1)

# max_host_ip
max_host_ip1 = broadcast1[0:3]
max_host_ip1.append(broadcast1[-1] - 1)
max_host_ip2 = broadcast2[0:3]
max_host_ip2.append(broadcast2[-1] - 1)


print("network\t\t\t\twildcard\t\tbroadcast\t\tmin_host_ip\t\tmax_host_ip")
print(
    network1,
    "\t\t",
    wildcard1,
    "\t",
    broadcast1,
    "\t",
    min_host_ip1,
    "\t",
    max_host_ip1,
)
print(
    network2,
    "\t\t",
    wildcard2,
    "\t\t",
    broadcast2,
    "\t",
    min_host_ip2,
    "\t",
    max_host_ip2,
)
