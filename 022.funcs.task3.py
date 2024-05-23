from time import perf_counter

def timer():
    start = perf_counter()
    def inner():
        nonlocal start
        print(f"{perf_counter() - start:.2f}")
        start = perf_counter()
    return inner

t = timer()

for i in range(10):
    t()
