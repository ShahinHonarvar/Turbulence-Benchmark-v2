def if_perfect_num(numbers):
    return numbers[0] == sum((i for i in range(1, numbers[0]) if numbers[0] % i == 0))