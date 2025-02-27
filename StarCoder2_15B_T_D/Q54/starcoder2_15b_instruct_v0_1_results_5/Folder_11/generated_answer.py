def all_right_truncatable_prime(nums):
    x = nums[86]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted(filter(is_right_truncatable_prime, range(x)))