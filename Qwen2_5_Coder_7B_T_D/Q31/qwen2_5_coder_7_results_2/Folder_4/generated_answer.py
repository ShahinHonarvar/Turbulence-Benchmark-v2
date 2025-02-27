def if_perfect_num(numbers):
    return sum(numbers[15]) == sum([i for i in range(1, numbers[15]) if numbers[15] % i == 0])