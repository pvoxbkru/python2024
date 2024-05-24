
seq = ["rt1", "RT2", "SW1", "sw2"]


result = list(filter(lambda e: e.lower().startswith("rt"), seq))
#['rt1', 'RT2']
print(result)
