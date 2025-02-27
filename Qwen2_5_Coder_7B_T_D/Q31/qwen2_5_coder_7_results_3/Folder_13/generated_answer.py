def if_perfect_num(numbers):
    return sum(numbers[126]) == sum((i for i in range(1, numbers[126]) if numbers[126] % i == 0))