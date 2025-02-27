def find_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return []
    divisors = [i for i in range(10, 70) if n % i == 0]
    return divisors