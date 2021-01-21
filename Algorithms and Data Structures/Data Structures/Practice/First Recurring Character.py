def first_recurring(letters):
    string = letters
    i = 1
    b = 0
    while string[i] != string[b]:
        print('String B before: ' + string[b] + ' ' + str(b))
        print('String i before: ' + string[i] + ' ' + str(i))
        i += 1
        if i >= len(letters):
            b += 1
            if i >= len(letters):
                return False
            i = b + 1
        print('String B: ' + string[b] + ' ' + str(b))
        print('String i: ' + string[i] + ' ' + str(i))
    return True


print(first_recurring('abc'))
