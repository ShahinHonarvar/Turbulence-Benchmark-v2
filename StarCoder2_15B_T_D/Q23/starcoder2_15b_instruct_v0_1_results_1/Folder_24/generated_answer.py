def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and i >= 43 and (i <= 95)]
    return divisors