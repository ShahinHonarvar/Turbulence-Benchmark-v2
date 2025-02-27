def if_perfect_num(numbers):
    return numbers[29] == sum((i for i in range(1, numbers[29]) if numbers[29] % i == 0))