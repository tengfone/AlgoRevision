def binary_search(lst,target):
    first = 0
    last = len(lst) - 1
    counter = 0
    while first <= last:
        midpoint = (first + last) // 2
        counter += 1
        if lst[midpoint] == target:
            return midpoint
            
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
    
print(binary_search([1,2,3,4,5],2))