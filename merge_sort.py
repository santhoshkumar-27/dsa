def merge_sort(lists):
    """
    Take a list  and sort in the ascending order
    Return in the new sorted array

    Divide: Find the midpoint of the list and divide into sublists
    conquer: Rescursively sort sublists the created in previous step
    combine: Merge the sorted sublists sorted created in previous step
    """
    length = len(lists)
    if length <= 1:
        return lists

    left_array, right_array = split(lists)
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid = len(list) // 2

    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(leftArray, rightArray):
    """
    Merge two lists (arrays) in order and return as single list
    """
    leftIndex = 0
    rightIndex = 0
    sortedArray = []
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        if leftArray[leftIndex] < rightArray[rightIndex]:
            sortedArray.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            sortedArray.append(rightArray[rightIndex])
            rightIndex += 1

    if leftIndex < len(leftArray):
        sortedArray.extend(leftArray[leftIndex:])
    elif rightIndex < len(rightArray):
        sortedArray.extend(rightArray[rightIndex:])

    return sortedArray



print(merge_sort([3, 2, 7, 8, 9, 1, 4, 6, 5]))