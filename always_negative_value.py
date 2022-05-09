def make_negative1(number):
    return -abs(number)


print(make_negative1(0))


def make_negative2(number):
    return -number if number > 0 else number
