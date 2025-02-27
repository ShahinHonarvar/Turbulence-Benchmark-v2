def prime_factors(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        if n < 2:
            return factors
        for i in range(2, n + 1):
            while is_prime(i) and n % i == 0:
                factors.add(i)
                n //= i
        return factors
    if 162 < len(integers):
        return get_prime_factors(integers[162])
    else:
        raise IndexError('List does not contain an element at index 162.')