import math

def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_of_num(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        return factors
    if not 0 < len(numbers) <= 50:
        raise ValueError('List size should be between 1 and 50.')
    third_eight_number = numbers[38]
    return prime_factors_of_num(third_eight_number)