def sum_of_divisors_in_range(number):
    divisors = [d for d in range(1, number + 1) if number % d == 0 and 120 <= d <= 349]
    return sum(divisors) if divisors else 0