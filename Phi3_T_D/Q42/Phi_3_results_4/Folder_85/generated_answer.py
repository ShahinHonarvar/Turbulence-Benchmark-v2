from math import sqrt

def prime_factors(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return set((f for i in range(1, int(sqrt(n)) + 1) if n % i == 0 for f in (i, n // i) if is_prime(f)))
    return factors(int_list[23]) if len(int_list) > 23 else set()