from math import sqrt

def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        return [i for i in range(2, num + 1) if num % i == 0 and is_prime(i)]
    return set(factors(numbers[849]))