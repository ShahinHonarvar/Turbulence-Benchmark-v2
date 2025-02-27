from math import sqrt

def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([lst[i] for i in range(32, 36) if is_prime(lst[i])])