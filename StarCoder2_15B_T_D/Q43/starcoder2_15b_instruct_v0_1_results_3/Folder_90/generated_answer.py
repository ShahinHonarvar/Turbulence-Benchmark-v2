def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_nums = [n for i, n in enumerate(nums) if is_prime(n) and 413 <= i <= 448]
    return sorted(prime_nums)