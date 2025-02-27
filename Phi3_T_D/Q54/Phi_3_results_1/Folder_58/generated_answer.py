def all_right_truncatable_prime(nums):
    x = nums[975]
    trunc_primes = []
    is_prime = lambda n: n > 1 and all((n % d for d in range(2, int(n ** 0.5) + 1)))

    def right_truncate(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(x - 1, 11, -1):
        if right_truncate(num) and num > 10:
            trunc_primes.append(num)
    return trunc_primes