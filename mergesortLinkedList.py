from linkedList import LinkedList


def merge_sort(linked_list):
    """
    Sort a linked list in ascending order
    - Recursively divide the linked list into sublist containing a single node
    - Repeatedly merge the sublists to proudce sorted sublists until one remains

    Returns a sorted linked list
    Runs in O(knlogn)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists 
    O(klogn)
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)  # -1 cause of size index

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges 2 linked lists, sorting by data in nodes
    Returns a new , merged list
    O(n) time
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtained head nodes for left and right linked list
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is nonde, we past the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head

            # Call next on right to set loop condition to False
            right_head = right_head.next_node

        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head

            # Call next on left to set loop condition to False
            left_head = left_head.next_node

        # If data on left is greater than right, set current to right node
        else:

            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node

            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node

        # move current to next node
        current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


n = LinkedList()
n.add(1)
n.add(5)
n.add(3)
n.add(99)
n.add(4)
print(n)
a = merge_sort(n)
print(a)
