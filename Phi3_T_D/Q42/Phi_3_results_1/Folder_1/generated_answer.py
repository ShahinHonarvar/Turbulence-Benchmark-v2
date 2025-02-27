from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) > 85 and is_prime(numbers[85]):
        factors = set()
        divisor = 2
        while numbers[85] > 1:
            while numbers[85] % divisor == 0:
                factors.add(divisor)
                numbers[85] //= divisor
            divisor += 1
        return factors
    else:
        raise ValueError('Index 85 must point to a valid number and the number at this index must be prime.')