def sum_of_divisors_in_range(num):
    return sum((d for d in range(1, num + 1) if num % d == 0 and 11 <= d <= 56))