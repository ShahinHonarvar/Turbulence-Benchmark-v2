from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    factor_set = set()
    number_to_factor = numbers[985]
    divisor = 2
    while divisor <= number_to_factor:
        if number_to_factor % divisor == 0 and is_prime(divisor):
            factor_set.add(divisor)
            number_to_factor //= divisor
        else:
            divisor += 1
    return factor_set