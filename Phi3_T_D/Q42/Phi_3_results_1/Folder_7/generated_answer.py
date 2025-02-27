import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(numbers_list):
    try:
        number = numbers_list[851]
        factors = set()
        for i in range(2, int(math.sqrt(number)) + 1):
            while number % i == 0:
                if is_prime(i):
                    factors.add(i)
                number //= i
        if number > 1:
            factors.add(number)
        return factors
    except IndexError:
        return 'No index 851 in the provided list.'