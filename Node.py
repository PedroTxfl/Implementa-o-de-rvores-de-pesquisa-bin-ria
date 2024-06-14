class Node: 
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

    def getKey(self):                                       #usa set e get
        return self.key

    def setKey(self, key):
        self.key = key

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

