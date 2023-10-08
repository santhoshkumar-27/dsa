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
        print('Target is found at position: ', index + 1)
    else:
        print("Target not found")

if __name__ == '__main__':
    verify(linear_search(range(1, 11), 2))
    verify(linear_search(range(1, 11), 12))