def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[47]) if numbers[47] % i == 0]) == numbers[47]