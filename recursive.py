def sum(numbers):
    print(not numbers)
    if not numbers: # if numbersis not present or empty list we should return it
        return 0
    # total = 0
    # for num in numbers:
    #     total += num
    
    # return total
    return numbers[0] + sum(numbers[1:])



print(sum([]))
print(sum([1]))
print(sum([1, 2, 3, 4, 5]))