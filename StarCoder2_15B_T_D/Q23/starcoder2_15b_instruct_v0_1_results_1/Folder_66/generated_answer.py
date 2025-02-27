def find_divisors_in_range(num):
    return [d for d in range(1, num + 1) if num % d == 0 and 32 <= d <= 35]