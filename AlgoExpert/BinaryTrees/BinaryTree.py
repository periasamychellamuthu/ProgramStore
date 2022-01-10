from TreeNode import TreeNode as node

nodeHeight=0
nodeDepth=0

class BinaryTree:
    head = None
    def __init__(self,value):
        if value is None:
            return None
        if self.head is None:
            self.head = node(value)
        else:
            self.addNodeToTheTree(value)
        return None

    def addNodeToTheBinarySearchTree(self,value):
        createdNode = node(value)
    
        if self.head is None:
            self.head = createdNode
        else:
            pos = self.head
            while pos is not None:
                if pos.value < value:
                    if pos.rightNode is None:
                        pos.addRightNode(createdNode)
                        break
                    else:
                        pos = pos.rightNode
                elif pos.value >= value:
                    if pos.leftNode is None:
                        pos.addLeftNode(createdNode)
                        break
                    else:
                        pos = pos.leftNode
        return None

    def addNodeToTheBinaryTree(self,value,loc):
        createdNode = node(value)
    
        if self.head is None:
            self.head = createdNode
        else:
            pos = self.head
            while loc!="" and pos!=None:
                if loc[0]=='L':
                    if pos.leftNode is None:
                        pos.addLeftNode(createdNode)
                        break;
                    else:
                        pos = pos.leftNode
                elif loc[0]=='R':
                    if pos.rightNode is None:
                        pos.addRightNode(createdNode)
                        break;
                    else:
                        pos = pos.rightNode
                loc=loc[1:]

    def treeTraversal(self,block):
        if block is None:
            return
        self.treeTraversal(block.leftNode)
        print(block.value)
        self.treeTraversal(block.rightNode)

    def branchSums(self,head):
        print(doBranchSumsProb(head,0,0))

    def findNodeHeight(self,value):
        # https://www.geeksforgeeks.org/program-to-calculate-height-and-depth-of-a-node-in-a-binary-tree/
        heightOfTheNodeInBinaryTree(self.head,value)
        print(nodeHeight)
        print(depthOfTheNodeInBinaryTree(self.head,value))




def doBranchSumsProb(head,total,current):
    # https://www.geeksforgeeks.org/sum-numbers-formed-root-leaf-paths/
    if head is None:
        return current
    total =  (total*10)+head.value
    if head.leftNode is None and head.rightNode is None:
        print(total)
        current = current+total
    else:
        current = doBranchSumsProb(head.leftNode,total,current)
        current = doBranchSumsProb(head.rightNode,total,current)
    return current

def heightOfTheNodeInBinaryTree(head,value):
    if head is None:
        return -1
    else:
        leftHeight = heightOfTheNodeInBinaryTree(head.leftNode,value)
        rightHeight = heightOfTheNodeInBinaryTree(head.rightNode,value)
        height = max(leftHeight,rightHeight)+1
        if head.value == value:
            global nodeHeight
            nodeHeight=height     
    return height

def depthOfTheNodeInBinaryTree(head,value):
    if head is None:
        return -1
    else:
        dist = -1
        if head.value == value:
            return dist+1
        dist = depthOfTheNodeInBinaryTree(head.leftNode,value)
        if dist>=0:
            return dist+1
        dist = depthOfTheNodeInBinaryTree(head.rightNode,value)
        if dist>=0:
            return dist+1
        return dist



