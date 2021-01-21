def hash_code(string):
    g = 31
    i = 0
    hash_total = 0
    for letter in string:
        hash_total = hash_total + ord(letter) * g**i
        i += 1

    return hash_total


print(hash_code('ab'))


def hash_code(string):
    ord() + 9(hash_code())
