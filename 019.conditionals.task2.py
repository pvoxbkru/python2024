ip = "10.3.2.1"

first_octet = int(ip.split(".")[0])

if first_octet >> 7 == 0b0:
    ip_class = "A"
elif first_octet >> 6 == 0b10:
    ip_class = "B"
elif first_octet >> 5 == 0b110:
    ip_class = "C"
elif first_octet >> 4 == 0b1110:
    ip_class = "D"
elif first_octet >> 4 == 0b1111:
    ip_class = "E"

print(f"класс ip {ip}: {ip_class}")
