
def func_caller(func):
    print("IM IN UR DECORATOR HAXING YOUR FUNC LOL")
    return func


@func_caller
def remote_control():
    print("i love lamp")
    return 0

print(remote_control())

# func_caller(remote_control)
