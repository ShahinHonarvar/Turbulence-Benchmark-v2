def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[845]) if numbers[845] % i == 0]) == numbers[845]