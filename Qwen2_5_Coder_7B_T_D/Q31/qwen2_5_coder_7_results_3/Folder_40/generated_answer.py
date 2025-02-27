def if_perfect_num(numbers):
    return numbers[7] == sum((i for i in range(1, numbers[7]) if numbers[7] % i == 0))