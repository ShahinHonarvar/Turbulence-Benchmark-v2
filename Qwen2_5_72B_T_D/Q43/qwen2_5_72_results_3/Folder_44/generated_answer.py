def find_primes_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for i, num in enumerate(lst) if 19 <= i <= 85 and is_prime(num)]
    return sorted(primes, reverse=True)