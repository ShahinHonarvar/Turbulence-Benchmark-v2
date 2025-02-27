def all_left_truncatable_prime(nums):
    x = nums[4]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if str(num).count('0') == 0 and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)