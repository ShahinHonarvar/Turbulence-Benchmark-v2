def all_right_truncatable_prime(nums):
    x = nums[97]

    def is_right_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(n)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_right_truncatable_prime, range(2, x)), reverse=True)