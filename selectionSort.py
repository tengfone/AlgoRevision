numbers = [3, 6, 1, 9, 2, 5]
numbers2 = [3, 6, 1, 9, 2, 5]

def selection_sort(values):
    sorted_list = []
    for i in range(0,len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1,len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

print(selection_sort(numbers))

def selection_sort2(values):
    sortedList = []

    for i in range(0,len(values)):
        smallestValue = findSmallestValue(values)
        sortedList.append(smallestValue)
        values.remove(smallestValue)
    return sortedList

def findSmallestValue(values):
    min = values[0]
    for i in range(0,len(values)):
        if values[i] < min:
            min = values[i]
    return min

print(selection_sort2(numbers2))