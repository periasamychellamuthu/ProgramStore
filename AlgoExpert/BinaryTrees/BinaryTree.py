nodeHeight=0
nodeDepth=0
maxPath=0

from TreeNode import TreeNode as node

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

    def findNodeHeightAndDepth(self,value):
        # https://www.geeksforgeeks.org/program-to-calculate-height-and-depth-of-a-node-in-a-binary-tree/
        heightOfTheNodeInBinaryTree(self.head,value)
        print(nodeHeight)
        print(depthOfTheNodeInBinaryTree(self.head,value))

    def findHeightOfTreeAlt(self,root):
        print(heightOfBinaryTree(root))

    def findDiameter(self,root):
        print(findMaxDiameterBetweenNodes(root))

    def inorderSuccessor(self,root,node):
        findInorderSuccessor(root,node)

    def maximumSumPathInBinaryTree(self,root):
        doMaximumSumPathInBinaryTree(root)
        print(maxPath)

    def printDistanceKNodeDown(self,root,target,dist):
        # print(dist,root)
        doPrintDistanceKUp(root,target,dist)

    def iterativeInorderTraversal(self,root):
        doIterativeInorderTraversal(root)

    def flatternBinartTreeToLinkedList(self,root):
        doFlatternToLinkedList(root)
        printOnlyRightNode(root)




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

def heightOfBinaryTree(treeNode):
    if treeNode is None:
        return 0
    return 1+max(heightOfBinaryTree(treeNode.leftNode),heightOfBinaryTree(treeNode.rightNode))

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

def invertTree(root):
    # https://leetcode.com/problems/invert-binary-tree/submissions/
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        invertTree(root.left)
        invertTree(root.right)
        temp=root.left
        root.left = root.right
        root.right = temp
        return root

def findMaxDiameterBetweenNodes(root):
    if root is None:
        return 0
    
    leftHeight = heightOfBinaryTree(root.leftNode)
    rightHeight = heightOfBinaryTree(root.rightNode)

    lDiameter = findMaxDiameterBetweenNodes(root.leftNode)
    rDiameter = findMaxDiameterBetweenNodes(root.rightNode)

    return max(leftHeight+rightHeight+1,max(lDiameter,rDiameter))

def findLeftMostNodeOfTreeNode(tNode):
    while(tNode!=None and tNode.leftNode!=None):
        tNode = tNode.leftNode
    return tNode

def findRightMostNodeOfTree(rNode):
    while rNode is not None and rNode.rightNode is not None:
        rNode = rNode.rightNode
    return rNode

def findInorderSuccessorOfNonRightBranchNode(root,tNode):
    if root is None:
        return None
    if root==tNode or findInorderSuccessorOfNonRightBranchNode(root.leftNode,tNode) or findInorderSuccessorOfNonRightBranchNode(root.rightNode,tNode):
        temp=findInorderSuccessorOfNonRightBranchNode(root.leftNode,tNode)
        if temp is None:
            temp=findInorderSuccessorOfNonRightBranchNode(root.rightNode,tNode)
        if temp:
            if root.leftNode==temp:
                print("result is",root.value)
                return None
            return temp
        return root
    return None

def findInorderSuccessor(root,tNode):
    # https://www.geeksforgeeks.org/inorder-succesor-node-binary-tree/
    #  also have one more alternate method , please refer the link
    if tNode.rightNode != None:
        print(findLeftMostNodeOfTreeNode(tNode.rightNode).value)
    else:
        findInorderSuccessorOfNonRightBranchNode(root,tNode)


def isBinaryTreeBalanced(root):
    # https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
    if root is None:
        return True

    leftHeight = heightOfBinaryTree(root.leftNode)
    rightHeight = heightOfBinaryTree(root.rightNode)

    lDiameter = isBinaryTreeBalanced(root.leftNode)
    rDiameter = isBinaryTreeBalanced(root.rightNode)

    if abs(leftHeight-rightHeight) <=1:
        return lDiameter and rDiameter

    return False

def doMaximumSumPathInBinaryTree(root):
    # https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
    # alternate method availbale please refer link
    if root is None:
        return 0

    leftSum = doMaximumSumPathInBinaryTree(root.leftNode)
    rightSum = doMaximumSumPathInBinaryTree(root.rightNode)
    global maxPath
    if(leftSum > maxPath):
        maxPath = leftSum
    elif rightSum > maxPath:
        maxPath = rightSum
    elif (root.value+leftSum+rightSum) > maxPath:
        maxPath = root.value+leftSum+rightSum
    elif root.value+leftSum > maxPath:
        maxPath = root.value+leftSum
    elif root.value+rightSum > maxPath:
        maxPath = root.value+rightSum


    return max(root.value,max(leftSum+root.value,rightSum+root.value))

def doPrintDistanceKNodeDown(root,pos):
    if root is None or pos < 0:
        return
    if pos == 0 :
        print(root.value)
    doPrintDistanceKNodeDown(root.leftNode,pos-1)
    doPrintDistanceKNodeDown(root.rightNode,pos-1)

def doPrintDistanceKUp(root,targetValue,distance):
    if root is None:
        return -1
    if root.value == targetValue:
        doPrintDistanceKNodeDown(root,distance)
        return 0
    dist = doPrintDistanceKUp(root.leftNode,targetValue,distance)
    if dist != -1:
        if dist+1 == distance:
            print(root.value)
        else:
            doPrintDistanceKNodeDown(root.rightNode,distance-dist-2)
        return 1+dist
        
    dist = doPrintDistanceKUp(root.leftNode,targetValue,distance)
    if dist != -1:
        if dist+1 == distance:
            print(root.value)
        else:
            doPrintDistanceKNodeDown(root.leftNode,distance-dist-2)
        return 1+dist
    return -1

def doIterativeInorderTraversal(root):
    node_stack = list()
    while root is not None or len(node_stack)>0:
        if root is None:
            root = node_stack.pop()
            print(root.value)
            root = root.rightNode
        else:
            node_stack.append(root)
            root = root.leftNode

def doFlatternToLinkedList(root):
    # https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
    # for alternate please refer url
        if root is None:
            return root
        lNode = doFlatternToLinkedList(root.leftNode)
        rNode = doFlatternToLinkedList(root.rightNode)
        if lNode is not None:
            rightMostofLeftNode = findRightMostNodeOfTree(lNode)
            rightMostofLeftNode.rightNode=rNode
            root.rightNode = lNode
        return root

def printOnlyRightNode(root):
    while root is not None:
        print(root.value)
        root = root.rightNode






    






