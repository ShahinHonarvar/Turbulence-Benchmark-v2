def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[41]) if numbers[41] % i == 0]) == numbers[41]