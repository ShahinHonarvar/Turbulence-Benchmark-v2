def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[51]) if numbers[51] % i == 0]) == numbers[51]