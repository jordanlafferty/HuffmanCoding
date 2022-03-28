list1 = {
    "J": 0.30,
    "I": 0.20,
    "H": 0.11,
    "G": 0.09,
    "F": 0.08,
    "E": 0.07,
    "D": 0.06,
    "C": 0.04,
    "B": 0.03,
    "A": 0.02
}


class Node:
    def __init__(self, symbol, value, left=None, right=None):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right
        self.huff = ' '

    def isLeaf(self):
        return self.left is None and self.right is None

    def UpdateHuff(self):
        if not self.isLeaf():
            self.left.huff = self.huff + '0'
            self.left.UpdateHuff()
            self.right.huff = self.huff + '1'
            self.right.UpdateHuff()

    def printHuff(self):
        if not self.isLeaf():
            self.left.printHuff()
            self.right.printHuff()
        else:
            print(f'{self.symbol}--{self.value}--> {self.huff}')


class HuffmanTree:
    def __init__(self):
        self.root = None

    def buildTree(self, insert):
        leafArray = []
        for key in insert:
            leafNode = Node(key, insert[key])
            leafArray.append(leafNode)

        while len(leafArray) > 1:
            leafArray.sort(key=lambda x: x.value, reverse=True)
            right = leafArray.pop()
            left = leafArray.pop()
            parentNode = Node(left.symbol + right.symbol, left.value + right.value, right, left)
            leafArray.append(parentNode)

        self.root = leafArray[0]

    def updateHuff(self):
        self.root.UpdateHuff()

    def printTable(self):
        self.root.printHuff()


tree = HuffmanTree()
tree.buildTree(list1)
tree.updateHuff()
tree.printTable()

