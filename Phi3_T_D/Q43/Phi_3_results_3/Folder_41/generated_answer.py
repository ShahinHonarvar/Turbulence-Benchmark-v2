def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    primes = [n for i, n in enumerate(nums[45:81]) if is_prime(n)]
    return sorted(primes, reverse=True)