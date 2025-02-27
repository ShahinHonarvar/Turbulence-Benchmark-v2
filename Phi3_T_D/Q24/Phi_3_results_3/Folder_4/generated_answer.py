def sum_of_divisors_in_range(number):
    return sum((d for d in range(48, 61) if number % d == 0))