def if_perfect_num(numbers):
    return sum(numbers[60]) == sum([i for i in range(1, numbers[60]) if numbers[60] % i == 0])