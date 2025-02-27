def if_perfect_num(numbers):
    perfect = sum([i for i in range(1, min(numbers[126], 126) + 1) if numbers[126] % i == 0]) == numbers[126]
    return perfect