
from datetime import datetime
from time import sleep


def my_log(msg, *, dt=None):
    if not dt:
        dt=datetime.now()
    print(f"[{dt:%Y-%m-%d %H:%M:%S}]: {msg}")

my_log("test")
sleep(3)
my_log("test")
sleep(4)
my_log("test")
