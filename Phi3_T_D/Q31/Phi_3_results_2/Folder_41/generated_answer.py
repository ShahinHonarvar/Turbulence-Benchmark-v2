def if_perfect_num(numbers):
    if 84 >= len(numbers):
        return False
    proper_divisors = [i for i in range(1, numbers[84] // 2 + 1) if numbers[84] % i == 0]
    return sum(proper_divisors) == numbers[84]