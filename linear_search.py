def linear_search(list, target):
    """
    return the position of the item in the list if not found Return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target is found at index: ', index)
    else:
        print("Target not found")




