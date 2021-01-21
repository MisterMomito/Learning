def merge_sort(a):
    merge_sort2(a, 0, len(a)-1)
    print(a)


def merge_sort2(a, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(a, first, middle)
        merge_sort2(a, middle+1, last)
        merge(a, first, middle, last)


def merge(a, first, middle, last):
    left = a[first:middle]
    right = a[middle:last+1]

    left.append(999999999999)
    right.append(999999999999)

    i = j = 0

    for k in range(first, last+1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1

        else:
            a[k] = right[j]
            j += 1



merge_sort([132, 13431, 431, 46, 3214, 8796, 15621, 4, 45, 9, 762, 178])

