# this is John Kwissin's version but with a pivot that is the middle of the two others


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        if pivot <= sequence[0] <= sequence[len(sequence)//2]:
            pivot = sequence[0]
        elif pivot <= sequence[len(sequence)//2] < sequence[0]:
            pivot = sequence[len(sequence)//2]

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([3, 4, 5, 87, 3234, 8, 0, 12, 182]))
