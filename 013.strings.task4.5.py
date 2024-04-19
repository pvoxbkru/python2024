ip = "77.88.55.242"

list_of_octet = ip.split(".")
list_of_octet_revers = list_of_octet[::-1]
ip_rtp = ".".join(list_of_octet_revers)
result = ip_rtp + ".in-addr.arpa"
print(result)