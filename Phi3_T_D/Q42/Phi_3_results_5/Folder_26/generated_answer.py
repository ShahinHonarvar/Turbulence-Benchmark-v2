from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
        return factors
    index = 222
    if index < len(numbers):
        return get_prime_factors(numbers[index])
    return 'Index out of range'