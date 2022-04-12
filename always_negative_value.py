def make_negative1(number):
    return -abs(number)
# but if number ==0, (-abs) make mistake


def make_negative2(number):
    return -number if number > 0 else number
