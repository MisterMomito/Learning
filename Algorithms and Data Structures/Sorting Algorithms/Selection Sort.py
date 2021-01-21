'''
def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for n in range(len(unsorted_list)-i):
        # from unsorted to the end:
        # find the minimum and set it as some variable
        # swap the unsorted[i] with that variable
'''

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)  # techincally not -1
    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value != i:
            list_a[i], list_a[min_value] = list_a[min_value], list_a[i]

    return list_a


print(selection_sort([7, 7, 7, 8, 1, 4,2, 7, 89, 1, 32, 3]))


