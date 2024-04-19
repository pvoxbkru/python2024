ip = "10.23.43.234"

list_of_dec = ip.split(".")
list_of_bin = [ f"{int(dec):0>8b}" for dec in list_of_dec]
result = "".join(list_of_bin)
print(result)