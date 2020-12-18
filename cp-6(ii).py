"""
WAP to binary search a number from a list using recursion technique.
"""


def binary_search(a_list, start, end, key):
    if not start < end:
        return -1
    mid = (start + end) // 2
    if a_list[mid] < key:
        return binary_search(a_list, mid + 1, end, key)
    elif a_list[mid] > key:
        return binary_search(a_list, start, mid, key)
    else:
        return mid


a_list = input('Enter the sorted list of number: ')
a_list = a_list.split()
a_list = [int(x) for x in a_list]
key = int(input('The number to search for: '))
index = binary_search(a_list, 0, len(a_list), key)
if index < 0:
    print('{} was not found'.format(key))
else:
    print('{} was found at index {}'.format(key, index))
