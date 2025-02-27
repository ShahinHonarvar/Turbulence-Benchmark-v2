def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n > 2 and n % 3 == 0
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    primes = [i for i in lst[23:59 + 1] if is_prime(i)]
    return sorted(primes, reverse=True)