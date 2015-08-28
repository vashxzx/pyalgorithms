
def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    return found

def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


if __name__ == '__main__':
    test_list1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list1, 3))
    print(sequential_search(test_list1, 13))

    test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(ordered_sequential_search(test_list2, 3))
    print(ordered_sequential_search(test_list2, 13))

    test_list3 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binary_search(test_list3, 3))
    print(binary_search(test_list3, 13))