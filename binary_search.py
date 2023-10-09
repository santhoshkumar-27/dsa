import linear_search

def binary_search(list, target, start, last):
    """
        Divide and conquor method and sorted input to get position on the element in the array of elements
    """
    if start > last: # last will either go to behond -1 or start will go larger then last
        return None
    midPoint = (start + last) // 2
    print(midPoint, start, last)
    currentNumber = list[midPoint]
    if target  ==  currentNumber:
        return midPoint
    elif target < currentNumber:
        return binary_search(list, target, start, midPoint - 1)
    elif target > currentNumber:
        return binary_search(list, target, midPoint + 1, last)

lists = range(1, 11)
linear_search.verify(binary_search(lists, 2, 0, len(lists) - 1))
