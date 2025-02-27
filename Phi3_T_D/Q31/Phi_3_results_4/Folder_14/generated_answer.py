def if_perfect_num(numbers):
    return sum((i for i in range(1, numbers[17]) if numbers[17] % i == 0)) == numbers[17] * 2