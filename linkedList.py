class Node:
    """
    An object for storing a single node of a linked list.
    2 Attributes, Data and the link
    """
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return "<Node Data: %s>" % self.data


class LinkedList:
    """
    Single Linked List
    """

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return number of nodes in the list, takes O(n) time
        """
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds a new Node containing data at head of list (PREPEND)
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head  # NEWNODE[] => OLDHEAD[]
        self.head = new_node  # NEWHEAD[] => OLDNODE[]

    def insert(self, data, index):
        """
        Inserting a new Node containing data at index position
        Insertion takes O(1) time but finding the node at index takes O(n)

        Overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Return the node or None if key doesnt exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            # current not none (gone pass tail node)
            # Found is inside the loop

            # First case, same data and first head
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node

            # Second case
            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            # 3rd case
            else:
                previous = current
                current = current.next_node

        return current

    def search(self, key):
        """
        Search for first node containing data that matches
        the key. Return the node or 'None' if not found
        O(n) Time (worst case to the end)
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return f'Node {key} Not Found'

    def node_at_index(self, index):
        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self) -> str:
        """
        Return a String representation of the list
        Takes O(n) time
        """
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
