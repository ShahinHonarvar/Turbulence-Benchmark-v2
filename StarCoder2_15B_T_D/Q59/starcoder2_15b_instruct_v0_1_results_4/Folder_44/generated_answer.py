def all_left_truncatable_prime(nums):
    x = nums[39]

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes