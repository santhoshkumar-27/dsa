class Node:
    """
    Head and tail
    An object for storing a single node of a linked
    single next node pointer
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """ 
    Singly linked lists
    traversal list
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def sizeOfSingleList(self):
        """ 
        Returns the number of nodes in the lists
        Takes o(n) times
        """
        current = self.head
        if current == None:
            return 0
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def append_item_to_list(self, data):
        current = self.head
        if current == None:
            self.head = Node(data)
            return

        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

l1 = LinkedList()
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
l1.append_item_to_list(5)
print(l1.sizeOfSingleList())