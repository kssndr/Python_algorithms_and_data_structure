class Node:
    def __init__(self, value=None, left=None, right=None, symbol=None, frequency=None):
        self.value = value
        self.left = left
        self.right = right
        self.symbol = symbol
        self.frequency = frequency

    def __str__(self):
        return "Node[" + str(self.value) + "]"


a = Node()
a.frequency = 5
a.symbol = 'a'
a.value = 1

print(a.symbol)
