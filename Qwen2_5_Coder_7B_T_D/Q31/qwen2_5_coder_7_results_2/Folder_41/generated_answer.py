def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[84]) if numbers[84] % i == 0]) == numbers[84]