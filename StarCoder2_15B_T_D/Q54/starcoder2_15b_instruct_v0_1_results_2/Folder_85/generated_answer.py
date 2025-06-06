def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not is_prime(num):
                return False
            num //= 10
        return is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[94]
    return sorted(filter(is_right_truncatable_prime, range(x)))