def all_right_truncatable_prime(nums):
    x = nums[84]
    primes = {2, 3, 5, 7}

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = []
    for num in range(10, x):
        if is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)