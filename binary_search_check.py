
def binary_search(list, target):
    if len(list) == 0:
        return False
    middleIndex = (len(list)) // 2
    if target == list[middleIndex]:
        return True
    elif target < list[middleIndex]:
        return binary_search(list[:middleIndex - 1], target)
    
    return binary_search(list[middleIndex + 1:], target)


lists = range(1, 11)


print(binary_search(lists, 11))