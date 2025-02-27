def find_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return []
    divisors = [divisor for divisor in range(43, 78) if n % divisor == 0]
    return divisors