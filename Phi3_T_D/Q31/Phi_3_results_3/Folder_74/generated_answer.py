def if_perfect_num(numbers):
    if len(numbers) <= 48:
        return False
    n = numbers[48]
    divisors_sum = sum([x for x in range(1, n // 2 + 1) if n % x == 0])
    return divisors_sum == n