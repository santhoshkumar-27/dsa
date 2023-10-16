def sum(numbers):

    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        return 0
    # total = 0
    # for num in numbers:
    #     total += num
    
    # return total
    return numbers[0] + sum(numbers[1:])



print(sum([]))
print(sum([1]))
print(sum([1, 2, 3, 4, 5]))