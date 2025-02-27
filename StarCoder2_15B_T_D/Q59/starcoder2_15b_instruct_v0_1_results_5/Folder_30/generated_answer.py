def all_left_truncatable_prime(nums):
    x = nums[37]

    def is_truncatable_prime(num):
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
    truncatable_primes = []
    for i in range(1, x):
        num = i
        while num < x:
            if not is_truncatable_prime(num):
                break
            num //= 10
        else:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)