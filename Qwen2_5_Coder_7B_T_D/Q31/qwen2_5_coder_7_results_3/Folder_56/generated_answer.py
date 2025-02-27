def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[60]) if numbers[60] % i == 0]) == numbers[60]