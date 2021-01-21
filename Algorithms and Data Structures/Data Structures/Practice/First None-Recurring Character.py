# first recurring
def first_recurring(string):
    s = set()
    for letter in string:
        if letter in s:
            return letter
        s.add(letter)
    return None


print(first_recurring(''))


def first_none_recurring(string):
    s = set()
    for letter in string:
        if letter not in string:

            return letter
        s.add(letter)

    return None


print(first_none_recurring('bba'))
