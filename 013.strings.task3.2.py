output = b"\r\nHuawei Versatile Routing Platform Software\r\nVRP (R) software, Version 8.220 (CE6857EI V200R022C00SPC500)\r\nCopyright (C) 2012-2022 Huawei Technologies Co., Ltd.\r\nHUAWEI CE6857-48S6CQ-EI uptime is 248 days, 3 hours, 14 minutes\r\n"

decod_string = output.decode('utf8')
list_of_strings = decod_string.split()
string_from_list = "".join(list_of_strings)
print(string_from_list)
