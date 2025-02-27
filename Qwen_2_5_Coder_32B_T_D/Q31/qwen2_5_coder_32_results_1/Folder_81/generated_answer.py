def if_perfect_num(numbers):
    if len(numbers) <= 20:
        return False
    n = numbers[20]
    sum_of_divisors = sum((d for d in range(1, n) if n % d == 0))
    return sum_of_divisors == n