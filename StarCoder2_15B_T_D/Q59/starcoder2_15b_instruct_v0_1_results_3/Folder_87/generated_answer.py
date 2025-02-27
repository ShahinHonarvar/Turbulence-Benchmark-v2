def all_left_truncatable_prime(nums):
    x = nums[39]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes