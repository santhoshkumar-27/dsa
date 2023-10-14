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

    def find(self, searchValue):
        """ 
        Returns the True or False for value searching
        Takes o(n) times
        """
        current = self.head
        if current == None:
            return False

        while current:
            if current.data == searchValue:
                return True
            current = current.next_node

        return False
    def append_item_to_list(self, data):
        """ 
            Adding data to the list three types
            adding data to prepend (head)
            adding data to append (tail)
            insert data in the middle

            inserting data is efficient in the linked list

            were are using append method to add data to the list
        """
        current = self.head
        if current == None:
            self.head = Node(data)
            return
        # Adding node to tail
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def prepend_item_to_list(self, data):
        current = self.head
        if current == None:
            self.head = Node(data)
            return
        # Adding node to tail
        self.head = Node(data)
        self.head.next_node = current

    def __repr__(self) -> str:
        """
            Return a string  representation of the list
            Takes O(n) time
        """
        nodes = []

        current = self.head

        while current:

            if current == self.head:
                nodes.append("[Head] %s" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail] %s" % current.data)
            else:
                nodes.append("[body] %s" % current.data)
        
            current = current.next_node

        # return "<Node data: %s>" % nodes
        return ' -> '.join(nodes)

l1 = LinkedList()
l1.append_item_to_list(5)
l1.append_item_to_list(6)
l1.append_item_to_list(7)
l1.append_item_to_list(8)
l1.append_item_to_list(9)
l1.append_item_to_list(10)
l1.append_item_to_list(11)
l1.append_item_to_list(12)
l1.prepend_item_to_list(13)
print(l1.sizeOfSingleList())
print(l1)
print(l1.find(13))