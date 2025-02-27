def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for i, n in enumerate(nums) if is_prime(n) and 23 <= i <= 75]
    primes.sort(reverse=True)
    return primes