from math import sqrt

def prime_factors(numbers):

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
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
        return factors
    index = 37
    number = numbers[index]
    return get_prime_factors(number)