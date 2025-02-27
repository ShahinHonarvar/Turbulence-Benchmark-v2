def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(x, y):
        if y < 10:
            return is_prime(y)
        if y % 10 == 0:
            return False
        return is_truncatable_prime(x, y // 10) and is_truncatable_prime(x, y % 10 ** (len(str(y)) - 1))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[93]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(x, i) and is_prime(i)])