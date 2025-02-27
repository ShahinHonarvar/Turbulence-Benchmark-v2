def if_perfect_num(numbers):
    return sum(numbers[48]) == sum([i for i in range(1, numbers[48]) if numbers[48] % i == 0])