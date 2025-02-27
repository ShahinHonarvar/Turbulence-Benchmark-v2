def find_divisors_in_range(n):
    divisors = [d for d in range(461, 828) if n % d == 0]
    return divisors