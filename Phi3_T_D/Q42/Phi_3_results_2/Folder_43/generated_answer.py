def prime_factors(lst):
    num = lst[29]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while is_prime(i) and n % i == 0:
                factors.add(i)
                n //= i
        return factors
    return get_prime_factors(num)