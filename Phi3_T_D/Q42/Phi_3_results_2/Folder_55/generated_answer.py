from math import sqrt

def prime_factors(numbers):
    number_21 = numbers[21]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    return get_prime_factors(number_21)