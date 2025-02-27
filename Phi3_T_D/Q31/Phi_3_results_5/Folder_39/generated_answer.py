def is_perfect_num(numbers):
    if len(numbers) > 59:
        divisor_sum = sum((i for i in range(1, numbers[59]) if numbers[59] % i == 0))
        return divisor_sum == numbers[59]
    return False