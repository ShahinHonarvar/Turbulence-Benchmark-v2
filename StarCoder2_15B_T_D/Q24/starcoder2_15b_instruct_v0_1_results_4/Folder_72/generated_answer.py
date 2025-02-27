def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    divisors = [d for d in range(1, num + 1) if num % d == 0 and 32 <= d <= 90]
    return sum(divisors)