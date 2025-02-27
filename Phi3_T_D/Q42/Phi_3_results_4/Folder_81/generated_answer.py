def prime_factors(nums):
    p_factors = set()

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    num = nums[20]
    for i in range(2, int(num ** 0.5) + 1):
        if is_prime(i) and num % i == 0:
            p_factors.add(i)
    return p_factors