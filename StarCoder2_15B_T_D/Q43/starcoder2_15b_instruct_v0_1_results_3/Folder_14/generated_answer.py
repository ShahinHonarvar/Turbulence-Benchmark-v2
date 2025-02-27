def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(nums) if 10 <= i <= 66 and is_prime(n)]
    return sorted(primes)