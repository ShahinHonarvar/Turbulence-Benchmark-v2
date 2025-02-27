def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start, end = (30, 43)
    return sorted([num for num in lst[start:end + 1] if is_prime(num)])