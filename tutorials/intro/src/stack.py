class Stack:
    """ En implementation av en stack som en länkad lista av noder
    (instanser av Node-klassen)"""
    def __init__(self):
        self.top = None

    def __str__(self):
        s = ""
        p = self.top
        while not p == None:
            s += p.data + " "
            p = p.next
        return s

    def push(self,x):
        """L?gger x ?verst p? stacken """
        ny = Node(x)
        ny.next = self.top
        self.top = ny

    def pop(self):
        """Plockar ut och returnerar det ?versta elementet """
        x = self.top.data
        self.top = self.top.next
        return x

    def isEmpty(self):
        """Returnerar True om stacken ?r tom, False annars"""
        if self.top == None: 
            return True
        else: 
            return False

class Node:
    """ Representerar en nod med värde och next-pekare """
    def __init__(self, x, next = None):
        self.data = x
        self.next = next
