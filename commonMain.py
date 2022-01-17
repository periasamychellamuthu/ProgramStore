# from interview_competition_programs import MakeItAnagram as MIA
# import sys;
# from AlgoExpert.FamousAlgorithm.KadanesAlgo import kadaneAlgo as algo;
from AlgoExpert.BinaryTrees.BinaryTree import BinaryTree as BT;
from AlgoExpert.BinaryTrees.TreeNode import TreeNode as TN;
if __name__=="__main__":
    # str1=str(input("enter string 1"))
    # str2= str(input("Enter String 2"))

    # # Kadanes alogrithm
    length = int(input("enter the length"))
    input1 = list()
    # for _ in range(length):
    #     input1.append(int(input()))
    # print(algo().proc(input1))


    # Binary tree creation
    binaryTree = BT(None)

    for _ in range(length):
        stdin = str(raw_input()).split(' ');
        binaryTree.addNodeToTheBinaryTree(int(stdin[0]),str(stdin[1]))
    # binaryTree.findNodeHeightAndDepth(5)
    # binaryTree.findHeightOfTreeAlt(binaryTree.head)
    # binaryTree.findDiameter(binaryTree.head)
    # binaryTree.inorderSuccessor(binaryTree.head,(binaryTree.head.leftNode))
    # binaryTree.maximumSumPathInBinaryTree(binaryTree.head)
    # binaryTree.printDistanceKNodeDown(binaryTree.head,2,1)
    # binaryTree.iterativeInorderTraversal(binaryTree.head)
    binaryTree.flatternBinartTreeToLinkedList(binaryTree.head)

    # inputs
# 6 HprintDistanceKNodeDown
# 3 L
# 2 LL
# 5 LR
# 7 LRL
# 4 LRR
# 5 R
# 4 RR

# 1 H
# 2 L
# 3 LL
# 4 LLL
# 5 R
# 6 LR
# 7 LRR
# 8 LRRL
# 9 LRRR
# 10 LRRRL
# 11 LLR
# 12 LLRL
# 13 LLRLR

# 1 H
# 2 L
# 4 LL
# 5 LR
# 3 R
# 6 RR

# 10 H
# 2 L
# 20 LL
# 1 LR
# 10 R
# -25 RR
# 3 RRL
# 4 RRR

# 1 H
# 3 L
# 4 R
# 2 RL
# 5 RLR
