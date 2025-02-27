def if_perfect_num(numbers):
    if len(numbers) <= 54:
        return False
    n = numbers[54]
    sum_factors = sum((i for i in range(1, n) if n % i == 0))
    return sum_factors == n