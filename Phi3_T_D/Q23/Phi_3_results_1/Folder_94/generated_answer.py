def find_divisors_in_range(n):
    if n <= 0:
        return []
    return [i for i in range(35, 38) if n % i == 0]