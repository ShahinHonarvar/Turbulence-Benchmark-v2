def all_left_truncatable_prime(nums):
    x = nums[74]
    left_truncatable_primes = []

    def is_left_truncatable_prime(num):
        if num < 2 or (num > 2 and num % 2 == 0) or num > x:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    for i in range(x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)