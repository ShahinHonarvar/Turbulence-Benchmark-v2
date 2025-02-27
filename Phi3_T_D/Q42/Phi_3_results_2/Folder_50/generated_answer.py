from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers_list):
    if len(numbers_list) == 0 or 40 >= len(numbers_list):
        return None
    number_at_index_40 = numbers_list[40]
    factors = set()
    for i in range(2, int(sqrt(number_at_index_40)) + 1):
        if number_at_index_40 % i == 0 and is_prime(i):
            factors.add(i)
            while number_at_index_40 % i == 0:
                number_at_index_40 //= i
    if number_at_index_40 > 1:
        factors.add(number_at_index_40)
    return factors