def if_perfect_num(numbers):
    return numbers[64] == sum((i for i in range(1, numbers[64]) if numbers[64] % i == 0))