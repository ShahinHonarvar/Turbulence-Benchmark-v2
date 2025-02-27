def all_left_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x) if is_prime(n) and is_left_truncatable_prime(n)], reverse=True)