def sum_of_divisors_in_range(number):
    if number <= 0:
        return 0
    divisors = [d for d in range(1, number + 1) if number % d == 0 and 35 <= d <= 98]
    return sum(divisors) if divisors else 0