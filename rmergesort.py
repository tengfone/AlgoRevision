def merge_sort(list):

    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left_side = list[:middle]
    right_side = list[middle:]

    left = merge_sort(left_side)
    right = merge_sort(right_side)

    return merge(left,right)

def merge(left,right):
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

a = merge_sort([3,4,5,7,8,2,3])
print(a)