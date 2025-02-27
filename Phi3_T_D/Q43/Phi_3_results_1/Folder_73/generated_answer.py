def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes_in_range = [x for x in lst[18:91] if is_prime(x)]
    return sorted(primes_in_range, reverse=True)