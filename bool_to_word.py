"""Convert boolean values to strings 'Yes' or 'No'."""


def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


print(bool_to_word(False))
print(bool_to_word(True))

bool_to_word = {True: 'Yes', False: 'No'}.get

print(bool_to_word(False))
print(bool_to_word(True))


def bool_to_word(boolean):
    return ['No', 'Yes'][boolean]


print(bool_to_word(False))
print(bool_to_word(True))

bool_to_word = ['No', 'Yes'].__getitem__

print(bool_to_word(False))
print(bool_to_word(True))
