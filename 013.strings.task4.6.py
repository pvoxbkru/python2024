ip = "192.168.43.54 / 255.255.254.0"

list_address = ip.split(" / ")[0].split(".")
list_mask = ip.split(" / ")[1].split(".")

address = [int(a) for a in list_address]
mask = [int(m) for m in list_mask]

network = [x & y for x, y in zip(address, mask)]
wildcard = [255 ^ x for x in mask]
broadcast = [x | y for x, y in zip(address, wildcard)]
min_host_ip = network[0:3]
min_host_ip.append(network[-1] + 1)
max_host_ip = broadcast[0:3]
max_host_ip.append(broadcast[-1] - 1)

print(network)
#'192.168.42.0'

print(wildcard)
#'0.0.1.255'

print(broadcast)
#'192.168.43.255'

print(min_host_ip)
#'192.168.42.1'

print(max_host_ip)
#'192.168.43.254'
