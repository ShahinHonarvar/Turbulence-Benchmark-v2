from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def find_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
            if num == 1:
                break
        return factors
    if len(numbers) > 7:
        return find_prime_factors(numbers[7])
    else:
        return 'List too short. Index 7 does not exist.'