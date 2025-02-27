def find_primes_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index, end_index = (10, 12)
    prime_nums = [n for i, n in enumerate(nums) if is_prime(n) and start_index <= i <= end_index]
    return sorted(prime_nums)