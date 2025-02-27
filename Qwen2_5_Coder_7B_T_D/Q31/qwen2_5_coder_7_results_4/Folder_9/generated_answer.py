def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[24]) if numbers[24] % i == 0]) == numbers[24]