class TreeNode:
    leftNode = None
    rightNode = None
    def __init__(self,value):
        self.value = value
        return None

    def addLeftNode(self,node):
        self.leftNode = node
        return node

    def addRightNode(self,node):
        self.rightNode=node
        return node

    
