import linear_search
    
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midPoint = (first + last) // 2

        if list[midPoint] == target:
            return midPoint
        elif list[midPoint] < target:
            first = midPoint + 1
        elif list[midPoint] > target:
            last = midPoint - 1

    return None

lists = range(1, 11)
linear_search.verify(binary_search(lists, 25))