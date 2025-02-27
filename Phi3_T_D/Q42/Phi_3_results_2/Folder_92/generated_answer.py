from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def smallest_prime_factor(n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0 and is_prime(i):
                return i
        if is_prime(n):
            return n
        return None

    def factors():
        is_power_of_prime = True
        prime = smallest_prime_factor(numbers[0])
        while prime:
            if numbers[0] % prime != 0:
                is_power_of_prime = False
                break
            numbers[0] //= prime
            if is_power_of_prime:
                yield prime
    return set(factors())