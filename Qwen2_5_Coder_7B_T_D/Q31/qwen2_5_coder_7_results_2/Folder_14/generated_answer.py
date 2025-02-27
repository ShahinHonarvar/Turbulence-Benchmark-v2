def if_perfect_num(numbers):
    return numbers[17] == sum([i for i in range(1, numbers[17]) if numbers[17] % i == 0])