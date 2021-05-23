import random

numbers = [3, 6, 1, 9, 2, 5]


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    counter = 0
    while not is_sorted(values):
        counter += 1
        random.shuffle(values)
    print(counter)
    return values

print(bogo_sort(numbers))