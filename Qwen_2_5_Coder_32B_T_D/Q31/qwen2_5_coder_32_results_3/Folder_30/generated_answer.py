def if_perfect_num(numbers):
    if len(numbers) < 95:
        return False
    n = numbers[94]
    sum_divisors = sum((d for d in range(1, n) if n % d == 0))
    return sum_divisors == n