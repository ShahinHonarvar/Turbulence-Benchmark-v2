def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    start_index = 31
    end_index = 67
    primes = [num for num in nums[start_index:end_index + 1] if is_prime(num)]
    return sorted(primes, reverse=True)