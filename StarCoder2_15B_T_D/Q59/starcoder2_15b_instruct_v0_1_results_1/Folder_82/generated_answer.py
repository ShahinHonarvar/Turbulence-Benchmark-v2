def all_left_truncatable_prime(nums):
    x = nums[69]

    def is_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        n = i
        while n > 0:
            if not is_truncatable_prime(n):
                break
            n //= 10
        else:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)