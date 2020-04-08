class Node(object):
    def __init__(self, child, parent, pos, next=None, number = None):
        super(Node, self).__init__()
        self.child = []
        self.parent = parent
        self.edge = {}  # format edge[child] = parent
        self.pos = pos
        self.next = next
        self.number = number
