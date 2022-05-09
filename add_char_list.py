def number(lines):
    new_lines = []
    for count, value in enumerate(lines):
        new = f'{count + 1}: {value}'
        new_lines.append(new)

    return new_lines


def number1(lines):
    return [f'{n}: {s}' for n, s in enumerate(lines, 1)]


lines0 = []
lines1 = ['a', 'b', 'c']
print(number(lines1))
print(number1(lines1))

# TODO: add task description
