def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[2]) if numbers[2] % i == 0]) == numbers[2]