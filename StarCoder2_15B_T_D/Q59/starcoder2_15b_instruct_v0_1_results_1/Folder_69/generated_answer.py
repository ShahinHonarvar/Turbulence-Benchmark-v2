def all_left_truncatable_prime(nums):
    x = nums[760]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_truncatable_prime, range(1, x)), reverse=True)