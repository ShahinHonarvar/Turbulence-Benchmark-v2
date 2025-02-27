def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[95]) if numbers[95] % i == 0]) == numbers[95]