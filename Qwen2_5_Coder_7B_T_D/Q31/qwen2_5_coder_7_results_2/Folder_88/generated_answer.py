def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[46]) if numbers[46] % i == 0]) == numbers[46] and numbers[46] != 1