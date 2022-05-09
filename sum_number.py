def sum_digits1(number):
    return sum(int(d) for d in str(abs(number)))


def sum_digits2(number):
    number = abs(number)
    return_number = 0

    while number > 0:
        return_number += number % 10
        number = int(number / 10)

    return return_number


def sum_one_digits(number):
    """count to one digit"""
    x = sum(int(digit) for digit in str(abs(number)))
    if x < 10:
        return x
    else:
        return sum_one_digits(x)


print(sum_one_digits(-12356))


def sum_digits(n):
    return 0 if n == 0 else int(n % 10) + sum_digits(n // 10)


# Driver code
number = 1234
print(sum_digits(number))


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def sum_digits2(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder
    return s


def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r
