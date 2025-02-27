def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n, factors):
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
    factors_set = set()
    number_to_factor = numbers[74]
    prime_factors_of(number_to_factor, factors_set)
    return factors_set