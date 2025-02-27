def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0 and 59 <= i <= 88]
    if not divisors:
        return 0
    return sum(divisors)