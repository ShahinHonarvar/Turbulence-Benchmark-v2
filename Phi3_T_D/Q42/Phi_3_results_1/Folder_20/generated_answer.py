from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(number):
        factors = set()
        i = 2
        while i <= number:
            if number % i == 0 and is_prime(i):
                factors.add(i)
                number //= i
            else:
                i += 1
        return factors
    if len(numbers) > 53:
        return get_prime_factors(numbers[53])
    else:
        raise IndexError('Index 53 out of range')