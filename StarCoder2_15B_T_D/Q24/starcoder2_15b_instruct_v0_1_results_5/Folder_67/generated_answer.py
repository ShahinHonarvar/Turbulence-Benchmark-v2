def sum_of_divisors_in_range(num):
    divisors = [x for x in range(1, num + 1) if num % x == 0 and 33 <= x <= 57]
    return sum(divisors) if divisors else 0