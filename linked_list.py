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