def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum([1,2,3,4,5]))

def recur_sum(numbers):

    if len(numbers) == 0:
        return 0

    remaining_sum = recur_sum(numbers[1:])
    return numbers[0] + remaining_sum

print(recur_sum([1,2,3,4,5]))