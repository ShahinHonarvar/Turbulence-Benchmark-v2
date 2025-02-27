def find_primes_between_indices(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_numbers = [num for num in nums[19:91] if is_prime(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers