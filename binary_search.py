import linear_search

def binary_search(list, target, start, last):
    if start > last:
        return None
    midPoint = (start + last) // 2
    currentNumber = list[midPoint]
    if target  ==  currentNumber:
        return midPoint
    elif target < currentNumber:
        return binary_search(list, target, start, midPoint - 1)
    elif target > currentNumber:
        return binary_search(list, target, midPoint + 1, last)

lists = range(1, 50000000000000)
linear_search.verify(binary_search(lists, 11, 0, len(lists) - 1))
