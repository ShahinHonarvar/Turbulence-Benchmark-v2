def find_divisors_in_range(n):

    def is_divisor_in_range(d):
        return 10 <= d <= 69
    return [d for d in range(1, n + 1) if n % d == 0 and is_divisor_in_range(d)]