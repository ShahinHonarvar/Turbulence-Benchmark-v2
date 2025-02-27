import math

def prime_factors(numbers):
    if len(numbers) == 0 or 90 >= len(numbers):
        return set()

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

    def factors(n):
        result = set()
        for i in range(2, math.isqrt(n) + 1):
            if is_prime(i) and n % i == 0:
                result.add(i)
                while n % i == 0:
                    n //= i
        if n > 1:
            result.add(n)
        return result
    return factors(numbers[90 - 1])