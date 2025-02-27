def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[93]) if numbers[93] % i == 0]) == numbers[93]