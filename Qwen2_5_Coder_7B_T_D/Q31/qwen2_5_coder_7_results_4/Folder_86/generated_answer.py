def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[194]) if numbers[194] % i == 0]) == numbers[194]