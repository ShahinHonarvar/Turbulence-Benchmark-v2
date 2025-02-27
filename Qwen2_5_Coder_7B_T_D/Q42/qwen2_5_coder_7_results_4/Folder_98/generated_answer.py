import math

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    if len(numbers) > 4 and numbers[4] > 1:
        number = numbers[4]
        factors = set()
        for i in range(2, int(math.sqrt(number)) + 1):
            while number % i == 0:
                if is_prime(i):
                    factors.add(i)
                number //= i
        if number > 1 and is_prime(number):
            factors.add(number)
        return factors
    return set()