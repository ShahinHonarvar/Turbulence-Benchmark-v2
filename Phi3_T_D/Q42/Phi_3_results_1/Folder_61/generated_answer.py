def prime_factors(int_list):

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
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
        return factors
    if len(int_list) > 8:
        return get_prime_factors(int_list[8])
    else:
        raise IndexError('The given list does not contain the 8th index.')