def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[478]) if numbers[478] % i == 0]) == numbers[478]