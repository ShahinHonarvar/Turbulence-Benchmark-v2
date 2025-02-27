def all_left_truncatable_prime(nums):
    x = nums[39]

    def is_left_truncatable_prime(num):
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
    return sorted(filter(is_left_truncatable_prime, range(1, x)))