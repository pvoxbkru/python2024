output = """
Local Interface         Exptime(s) Neighbor Interface            Neighbor Device
-------------------------------------------------------------------------------------
100GE1/0/1                    107  100GE1/0/1                    spine1.pod1.stg
10GE1/0/1                     105  10GE1/0/1                     test-server.stg
""".strip()

template = "-------------------------------------------------------------------------------------\n"
result = output.replace(template, "")

print(result)