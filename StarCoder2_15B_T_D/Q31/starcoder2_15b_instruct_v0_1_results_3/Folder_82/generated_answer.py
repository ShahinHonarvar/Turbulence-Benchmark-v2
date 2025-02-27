def if_perfect_num(numbers):
    total = 0
    for i in range(len(numbers)):
        if i == 83:
            factor = 1
        else:
            factor = numbers[i]
        total += factor
    return total == numbers[83]