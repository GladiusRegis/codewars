sheep = [
    True, True, False,
    True, False, True
]


def counting_sheep(array_of_sheep):
    count = 0
    for place in array_of_sheep:
        if place:
            count += 1
    return count


print(counting_sheep(sheep))


def counting_sheep2(array_of_sheep):
    return array_of_sheep.count(True)


print(counting_sheep2(sheep))
