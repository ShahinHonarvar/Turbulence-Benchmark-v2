def find_primes_between_indices(nums):
    if len(nums) < 69:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_prime, nums[13:69]))