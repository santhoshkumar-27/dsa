from linked_list import LinkedList


l1 = LinkedList()
l1.append_item_to_list(5)
l1.append_item_to_list(7)
l1.prepend_item_to_list(4)
l1.prepend_item_to_list(8)

print(l1)

# three functions
# main function
# split function
# sort function

def merge_sort(linked_list):
    """ 
    sorts a linked lists in ascending order
        -> recursively divide the linked list into sublists containing a single node
        -> Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked lists
    """

    if linked_list.sizeOfSingleList() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.sizeOfSingleList()
        mid = size // 2
        midNode = linked_list.returnAtIndex(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = midNode.next_node
        midNode.next_node = None

        return left_half, right_half


def merge(left_half, right_half):
    """
    Merges two linked lists, sorting by data in nodes
    Return a new, merged lists
    """
    # Create a new linked list that contains nodes from
    # meging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.append_item_to_list(0)

    # set current to the head of the linked list
    current = merged.head

    #Obtain head nodes for left and right linked lists
    left_head = left_half.head
    right_head = right_half.head

    # iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from right to left merget linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is None, we're past the tail
        # Add the node from left to right merget linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node  data to peform comparision operations
            left_data = left_head.data
            right_data = right_head.data
            # if data  on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data  on right is greater than left, set current to right node
            else:
                current.next_node = right_head
                # move left head to next node
                right_head = right_head.next_node

        # move current  to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged



print(merge_sort(l1))