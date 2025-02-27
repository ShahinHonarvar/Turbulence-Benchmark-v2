from math import sqrt

def prime_factors(numbers):

    def factors(n):
        result = set()
        for i in range(2, int(sqrt(n)) + 1):
            while n % i == 0:
                result.add(i)
                n //= i
        if n > 1:
            result.add(n)
        return result
    return factors(numbers[35])