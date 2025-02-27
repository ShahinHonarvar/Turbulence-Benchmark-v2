def if_perfect_num(numbers):
    if len(numbers) <= 48:
        return False
    n = numbers[48]
    sum_factors = sum((i for i in range(1, n) if n % i == 0))
    return sum_factors == n