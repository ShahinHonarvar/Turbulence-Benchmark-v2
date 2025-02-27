def if_perfect_num(numbers):
    if len(numbers) < 223:
        return False
    n = numbers[222]
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n