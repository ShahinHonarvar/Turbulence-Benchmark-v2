def find_primes_between_indices(nums):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    primes = [n for n in nums[23:76] if is_prime(n)]
    return sorted(primes, reverse=True)