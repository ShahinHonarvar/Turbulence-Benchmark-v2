def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()

        def factorize(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    while num % i == 0:
                        num //= i
            if num > 1:
                factors.add(num)
        factorize(n)
        return factors
    if len(num_list) < 68:
        raise ValueError('List must have at least 68 elements.')
    return prime_factors_of(num_list[67])