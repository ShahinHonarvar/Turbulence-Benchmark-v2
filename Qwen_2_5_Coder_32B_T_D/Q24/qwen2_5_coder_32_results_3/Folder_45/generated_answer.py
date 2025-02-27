def sum_of_divisors_in_range(n):
    divisors = [d for d in range(4, 9) if n % d == 0]
    return sum(divisors)