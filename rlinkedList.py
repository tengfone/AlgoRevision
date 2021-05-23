class Node:
    data = None
    next_node = None
    def __init__(self,data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return F"<Node Value:{self.data}>"

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert(self,data,index):
        """
        Inserting a new Node containing data at index position
        Insertion takes O(1) time but finding the node at index takes O(n)

        Overall O(n) time
        """
        if index == 0:
            self.addFront(data)
        if index < 0:
            raise IndexError('Does not support negative index yet')
        if index > 0:
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            newNode = Node(data)
            prevNode = current
            nextNode = current.next_node
            prevNode.next_node = newNode
            newNode.next_node = nextNode

    def addFront(self,data):
        """
        [add(HEAD)] => [old] => [Tail]
        """
        newNode = Node(data)
        newNode.next_node = self.head
        self.head = newNode

    def addBack(self,data):
        """
        [Head] => [Add(TAIL)]
        """
        current = self.head
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            while current:
                lastNode = current
                current = current.next_node
            lastNode.next_node = newNode

    def size(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next_node
        print(f"Size of LinkedList is {counter}")

    def remove(self,value):
        current = self.head
        found = False
        while current and not found:
            if current == self.head and current.data == value:
                found = True
                self.head = current.next_node
            elif current.data == value:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node                

    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '-> '.join(nodes)

n = LinkedList()
print("\nAdding Forward 1 2 3")
n.addFront(1)
n.addFront(2)
n.addFront(3)
print(repr(n))
n = LinkedList()
print("\nAdding Backwards 1 2 3")
n.addBack(1)
n.addBack(2)
n.addBack(3)
n.size()
print(repr(n))
print("\nInserting from [1,2,3] to [1,2,99,3]")
n = LinkedList()
n.addBack(1)
n.addBack(2)
n.addBack(3)
n.insert(99,2)
print(repr(n))
print("\nRemoving from [1,2,3] to [1,2]")
n = LinkedList()
n.addBack(1)
n.addBack(2)
n.addBack(3)
n.remove(3)
print(repr(n))