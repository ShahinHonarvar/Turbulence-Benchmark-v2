def is_perfect_num(numbers):
    if len(numbers) > 95 and numbers[95] < 0:
        return False
    divisors_sum = sum((i for i in range(1, numbers[95]) if numbers[95] % i == 0))
    return divisors_sum == numbers[95]