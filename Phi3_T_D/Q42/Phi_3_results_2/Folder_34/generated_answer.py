def prime_factors(integers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        return factors
    return get_prime_factors(integers[97])