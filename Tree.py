#coding=utf-8
"""
二叉树的构造及遍历方法
树的构造
- 递归实现先序遍历、中序遍历、后序遍历
- 堆栈实现先序遍历、中序遍历、后序遍历
- 队列实现层次遍历
"""
class Node(object):
    def __init__(self, elem = -1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

class Tree(object):
    """
    Tree
    """
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """
        add node in a tree
        """
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue,append(treeNode.left)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)

    def front_digui(self, root):
        if root == None:
            return 
        print(root.elem, end = "")
        self.front_digui(root.left)
        self.front_digui(root.right)

    def middle_digui(self, root):
        if root == None:
            return 
        self.middle_digui(root.left)
        print(root.left, end="")
        self.middle_digui(root.right)

    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        print(root.elem, end="")

    #### 非递归遍历 ####

    def front_stack(self, root):
        if root== None:
            return 
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.elem, end="")
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.right
    
    def middle_stack(self ,root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print(node.elem, end="")
            node = node.right

    def later_stack(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        while myStack1:
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:
            print(myStack2.pop().elem, end="")

    


    



