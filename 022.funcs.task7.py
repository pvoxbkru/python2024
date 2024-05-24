def foo(*, param1, param2=None, param3=None):
    for param in param1, param2, param3:
        if param != None:
            print(f"{param}")


foo(
    param2=2,
    param3=3,
    param1=None,
)
