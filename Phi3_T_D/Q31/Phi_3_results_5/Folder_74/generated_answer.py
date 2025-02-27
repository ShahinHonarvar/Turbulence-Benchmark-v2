def if_perfect_num(numbers):
    if len(numbers) > 48:
        divisors_sum = sum((i for i in range(1, numbers[48]) if numbers[48] % i == 0))
        return divisors_sum == numbers[48]
    return False