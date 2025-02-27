def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
        return factors
    if 69 < len(lst) and isinstance(lst[69], int) and (lst[69] > 0):
        return get_prime_factors(lst[69])
    return set()