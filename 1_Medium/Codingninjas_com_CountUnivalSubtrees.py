
"""
# Codingnijas.com # Problem # Count Univalue Subtrees # 697311 #
----------------------------------------------------------------
You are given a binary tree. 
Return the count of unival sub-trees in the given binary tree. 
In unival tree, 
all the nodes below the root node, have the same value as the data of the root.

 0
  / \
 1   0
    / \
   1   0
  / \
 1   1

There are 5 unival subtrees (4 ones and 1 zero) in the tree above!
"""

import queue
import sys
sys.setrecursionlimit(10**6)

cnt = 0

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
    
###########################################
####### MY SOLUTION GOES HERE #############
###########################################
def countUnivalTrees(root):
    global cnt
    cnt = 0
    traverse(root)
    return cnt

def traverse(n):
    if n is None:
        return True
    is_unival = True
    if n.left:
        leftval = traverse(n.left)
        if not leftval: 
            is_unival = False
        else:
            if n.left.data != n.data:
                is_unival = False
    if n.right:
        rightval = traverse(n.right)
        if not rightval:
            is_unival = False
        else:
            if n.right.data != n.data:
                is_unival = False
    if is_unival:
        global cnt
        cnt += 1
    return is_unival
###################################################
####################################################

def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    
t = int(input())
while t >0:
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t -1


            
            

