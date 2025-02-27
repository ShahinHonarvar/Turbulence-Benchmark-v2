def find_divisors_in_range(num):
    return [x for x in range(1, num + 1) if num % x == 0 and 48 <= x <= 92]