def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[77]
    right_truncatable_primes = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)