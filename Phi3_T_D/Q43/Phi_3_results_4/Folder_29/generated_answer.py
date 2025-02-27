def find_primes_between_indices(lst):
    assert 24 <= len(lst) <= 32, 'The list must be long enough for indices between 24 and 32'

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted((x for x in lst[24:33] if is_prime(x)), reverse=True)