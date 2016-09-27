
def adder(number_one, number_two, message="No Message Passed", happy=True):
    print(message)
    print(happy)
    return number_one + number_two


print(adder(9, 4, happy=False, message="DO WORK!!!"))

print(adder("Joel", " likes programing!"))


def add(*args):
    return sum(args)

print(add(1, 2, 4, 90, 53, 12))

print(adder(*[9, 4]))

print(add(*range(1000)))


def beginners_luck(name, account_number, *args, birthday="tomorrow", **kwargs):
    print(name, "NAME")
    print(account_number, "ACCOUNT NUMBEr")
    print(args)
    print(kwargs)
    return 1


print(beginners_luck("joel", 12093819023, [1, 2, 3], 99, birthday="Today", lol="joel"))












