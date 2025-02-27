def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    start_index = max(0, 25 - len(nums))
    end_index = max(0, min(62, len(nums))) + 1
    primes = sorted([num for num in nums[start_index:end_index] if is_prime(num)])
    return primes