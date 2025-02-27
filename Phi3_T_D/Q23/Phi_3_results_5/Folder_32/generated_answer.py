def find_divisors_in_range(n):
    divisors = [num for num in range(71, 82) if n % num == 0]
    return divisors