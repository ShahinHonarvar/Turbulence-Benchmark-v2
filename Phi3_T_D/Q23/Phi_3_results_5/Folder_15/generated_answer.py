def find_divisors_in_range(n):
    if n < 7:
        return []
    return [i for i in range(7, 10) if n % i == 0]