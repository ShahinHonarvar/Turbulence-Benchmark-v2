def find_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    filtered_divisors = list(filter(lambda x: 35 <= x <= 55, divisors))
    return filtered_divisors