class Node:
    """ Representerar en nod med värde och next-pekare """
    def __init__(self, value, nxt=None):
        self.data = value
        self.next = nxt
