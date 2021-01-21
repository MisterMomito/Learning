def quick_sort(a):
    quick_sort2(a, 0, len(a) - 1)


def quick_sort2(a, low, high):
    if high - low < 20 and low < high:
        quick_selection(a, low, high)  # this is an improvement for smaller sets.
        # this used to be just the bottom if statement

    elif low < high:
        p = partition(a, low, high)
        quick_sort2(a, low, p - 1)
        quick_sort2(a, p + 1, high)


def get_pivot(a, low, high):
    mid = (high + low) // 2
    pivot = high
    if a[low] < a[mid]:
        if a[mid] < a[high]:  # what if it's equal
            pivot = mid
    elif a[low] < a[high]:
        pivot = low
    return pivot


def partition(a, low, high):
    pivot_index = get_pivot(a, low, high)
    pivot_value = a[pivot_index]
    a[pivot_index], a[low] = a[low], a[pivot_index]
    border = low

    for i in range(low, high + 1):
        if a[i] < pivot_value:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border] = a[low]

    return border
