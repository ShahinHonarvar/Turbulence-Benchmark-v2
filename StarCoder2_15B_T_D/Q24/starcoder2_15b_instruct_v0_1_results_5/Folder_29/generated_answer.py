def sum_of_divisors_in_range(num):
    divisors = [d for d in range(1, num + 1) if num % d == 0 and 43 <= d <= 77]
    return sum(divisors) if divisors else 0