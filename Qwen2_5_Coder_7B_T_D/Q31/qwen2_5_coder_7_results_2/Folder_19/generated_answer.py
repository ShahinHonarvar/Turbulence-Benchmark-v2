def if_perfect_num(numbers):
    if len(numbers) > 13:
        sum_divisors = sum((i for i in range(1, numbers[13]) if numbers[13] % i == 0))
        return sum_divisors == numbers[13]
    return False