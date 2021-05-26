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

############################ DRIVER CODES ############################

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