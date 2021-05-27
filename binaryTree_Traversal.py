## NOTE: Binary Tree != Binarary Search Tree. BT has no order 

class Stack(object):
    def __init__(self) -> None:
        super().__init__()
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self) -> None:
        super().__init__()
        self.items = []

    def enqueue(self,item):
        """
        Adding items in queue
        """
        self.items.insert(0,item)

    def dequeue(self):
        """
        Remove items in queue
        """
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        """
        See first item
        """
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if (traversal_type == "preorderR"):
            return self.preorderR_print(tree.root, "")
        elif traversal_type == "preorderI":
            return self.preorderI_print(tree.root)
        elif traversal_type == "inorderR":
            return self.inorderR_print(tree.root, "")
        elif traversal_type == "inorderI":
            return self.inorderI_print(tree.root)
        elif traversal_type == "postorderR":
            return self.postorderR_print(tree.root,"")
        elif traversal_type == "postorderI":
            return self.postorderI_print(tree.root)
        elif traversal_type == "bfs":
            return self.level_order_print(tree.root)
        elif traversal_type == "reverseLevelOrder":
            return self.reverse_level_order_print(tree.root)
        elif traversal_type == "HeightOfTree":
            return self.heightOfTree_print(tree.root)
        elif traversal_type == "sizeOfTree":
            return self.sizeOfTree_print(tree.root)
        else:
            print("Traversal Type Not Supported")
            return False

    def preorderR_print(self, start, traversal):
        """
        Root -> Left -> Right
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorderR_print(start.left, traversal)
            traversal = self.preorderR_print(start.right, traversal)
        return traversal

    def preorderI_print(self,start):
        """
        Use stack, first in last out. O(n) time and space
        """
        stack = [start]
        result = ""

        while stack != []:
            start = stack.pop()
            result += (str(start.value) + "-")
            if start.right is not None:
                stack.append(start.right)
            if start.left is not None:
                stack.append(start.left)
        return result

    def inorderR_print(self,start,traversal):
        """
        Left > Root > Right
        """
        if start:
            traversal = self.inorderR_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorderR_print (start.right,traversal)
        return traversal

    def inorderI_print(self,start):
        """
        Use Stack again. First in Last Out. O(n) Space and Time
        """
        stack = []
        result = ""

        while stack != [] or start is not None:
            while start is not None:
                stack.append(start)
                start = start.left
            start = stack.pop()
            result += (str(start.value) + "-")
            start = start.right
            
        return result


    def postorderR_print(self,start,traversal):
        """
        Left > Right > Root
        """
        if start:
            traversal = self.postorderR_print(start.left,traversal)
            traversal = self.postorderR_print (start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def postorderI_print(self,start):
        """
        Use Stack again. First in Last Out. O(n) Space and Time
        """
        stack = []
        result = ""

        # TODO:
        # Implement 
        
        return result

    def level_order_print(self,start):
        """
        AKA BFS BREADTH FIRST SEARCH. Uses QUEUE,FIRST IN FIRST OUT FIFO
        https://www.youtube.com/watch?v=aM-oswPn19o&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=2
        """
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_level_order_print(self,start):
        """
        Reverse level order (NOT BFS/DFS). Use a queue AND stack
        https://www.youtube.com/watch?v=bK6lijUbvms&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=3
        """
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()

        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop() # Reverse
            traversal += str(node.value) + "-"
        
        return traversal

    def heightOfTree_print(self, node):
        """
        Find Height Of Tree 
        https://www.youtube.com/watch?v=BDw8zzy3QiY&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=4
        """
        if node is None:
            return -1
        
        left_height = self.heightOfTree_print(node.left)
        right_height = self.heightOfTree_print(node.right)

        return 1 + max(left_height,right_height)
    
    def sizeOfTree_print(self,node):
        """
        Find Size Of Tree (iteratively//recursive)
        https://www.youtube.com/watch?v=VbruT_rwfzQ&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=5
        """

        ## Iteratively
        # if self.root == None:
        #     return 0
        
        # stack = Stack()
        # stack.push(self.root)
        # counter = 1
        # while stack:
        #     node = stack.pop()
        #     if node.left:
        #         counter += 1 
        #         stack.push(node.left)
        #     if node.right:
        #         counter += 1
        #         stack.push(node.right)
        # return counter

        ## Recursively
        if node is None:
            return 0
        return 1 + self.sizeOfTree_print(node.left) + self.sizeOfTree_print(node.right)

######################################################################
############################ DRIVER CODES ############################
######################################################################

## Main Youtube Link: https://www.youtube.com/watch?v=6oL-0TdVy28&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=1

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## PREORDER: [1,2,4,5,3,6,7,8]
## PREORDER: https://www.youtube.com/watch?v=pUSy6UZCFKw

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print("Recursive PreOrder")
recursive_preorder = tree.print_tree("preorderR")
print(recursive_preorder)

print("Iterative PreOrder")
iterative_preorder = tree.print_tree("preorderI")
print(iterative_preorder)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## INORDER: [4,2,5,1,6,3,7,8]
## INORDER: https://www.youtube.com/watch?v=RJhh3Jcc9zw

print("Recursive Inorder")
recursive_inorder = tree.print_tree("inorderR")
print(recursive_inorder)

print("Iterative Inorder")
iterative_inorder = tree.print_tree("inorderI")
print(iterative_inorder)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## POSTORDER: [4,5,2,6,8,7,3,1]
## POSTORDER: 

print("Recursive PostOrder")
recursive_postorder = tree.print_tree("postorderR")
print(recursive_postorder)

print("Iterative PostOrder")
iterative_postorder = tree.print_tree("postorderI")
print(iterative_postorder)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## LEVEL_ORDER: [1,2,3,4,5,6,7,8]

print("Level Order/BFS")
bfs = tree.print_tree("bfs")
print(bfs)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## REVERSE_LEVEL_ORDER: [8,4,5,6,7,2,3,1]

print("Reverse Level Order")
reverseLevelOrder = tree.print_tree("reverseLevelOrder")
print(reverseLevelOrder)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## Height Of Tree: 3

print("Height Of Tree")
treeHeight = tree.print_tree("HeightOfTree")
print(treeHeight)

#     1
#    / \
#   2   3
#  /\   /\
# 4  5  6 7
#          \
#           8
## Size Of Tree: 8

print("Size Of Tree")
treeSize = tree.print_tree("sizeOfTree")
print(treeSize)