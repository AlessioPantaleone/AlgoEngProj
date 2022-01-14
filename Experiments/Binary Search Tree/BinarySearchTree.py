from Imports.myimports import *


class SimpleNode:
    def __init__(self, key: int, element="Pippo"):
        self.element = key
        self.key = key
        self.leftchild = None
        self.rightchild = None

    def __str__(self):
        return f"I am {self.element} and my key is {self.key}"

    def addleftchild(self, node):
        self.leftchild = node

    def addrightchild(self, node):
        self.rightchild = node

    def getkey(self):
        return self.key

    def getelement(self):
        return self.element


class BinarySearchTree:
    def __init__(self, keyarr=None):
        if keyarr is None:
            keyarr = [49, 21, 52, 56, 54, 67, 77, 75, 83]
        self.root = SimpleNode(keyarr.pop(0), "Radice")
        while keyarr:
            newnode = SimpleNode(keyarr.pop(0), "Nodo")
            self.insert(newnode)

    def __str__(self):
        return ""

    def search(self, key: int):
        v = self.root
        while v is not None:
            if key == v.getkey():
                return v.getelement()
            else:
                if key < v.getkey():
                    v = v.leftchild
                if key > v.getkey():
                    v = v.rightchild
        return None

    def searchparent(self, key: int):
        v = self.root
        while v is not None:
            if key < v.getkey():
                if v.leftchild is None:
                    return v
                v = v.leftchild
            if key > v.getkey():
                if v.rightchild is None:
                    return v
                v = v.rightchild

    def insert(self, node: SimpleNode):
        insertingkey = node.getkey()
        parent = self.searchparent(insertingkey)
        if insertingkey > parent.getkey():
            node.rightchild = parent.rightchild
            parent.rightchild = node
        if insertingkey < parent.getkey():
            node.leftchild = parent.leftchild
            parent.leftchild = node

    def delete(self):
        ...

    def printTree(self, node: SimpleNode, level=0):
        if node is not None:
            self.printTree(node.leftchild, level + 1)
            print(' ' * 4 * level + '->', node.element)
            self.printTree(node.rightchild, level + 1)


if __name__ == "__main__":
    for iterations in range(15):
        RandomArr = random.sample(range(100), 20)
        BST = BinarySearchTree(RandomArr)
        BST.printTree(BST.root)
        print("////////////////////////////////////////")
