def merge_sort(lst):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the mid point of the list and divide into sublist
    Conquer: Recursively sort the sublist created in previous step
    Combine: Merge the sorted sublist created in previous step
    """

    if len(lst) <= 1:
        return lst

    left_half , right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Return 2 sublists - left and right
    """

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    ### NOTE:
    ### [SLICE] USES O(k) where k is the length of the size. so overall time complexity is O(knlogn)
    ### to get O(nlogn) need to use iterative

    return left, right

def merge(left,right):
    """
    Merge 2 list(arrays), sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(lst):
    n = len(lst)

    if n == 0 or n == 1:
        return True
    
    return lst[0] <= lst [1] and verify_sorted(lst[1:])

alist = [3,1,5,7,7,10,2,7]
l = merge_sort(alist)
print(l)
print(verify_sorted(l))