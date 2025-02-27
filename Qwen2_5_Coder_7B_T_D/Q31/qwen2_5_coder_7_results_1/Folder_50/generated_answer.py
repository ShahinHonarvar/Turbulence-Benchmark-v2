def if_perfect_num(numbers):
    return sum(numbers[40] == sum((i for i in range(1, numbers[40]) if numbers[40] % i == 0)))