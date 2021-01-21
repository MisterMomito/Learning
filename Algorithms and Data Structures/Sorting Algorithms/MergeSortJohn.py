# Johnathon Kwisses


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = int(len(array)) // 2
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    array = [5, 4, 3, 2, 1]
    print(array)

    result = merge_sort(array)
    print(result)


if __name__ == '__main__':
    main()
