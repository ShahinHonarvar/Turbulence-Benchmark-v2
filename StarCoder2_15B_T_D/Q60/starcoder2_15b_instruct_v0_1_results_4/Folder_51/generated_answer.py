def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        if n < 10:
            return n in (2, 3, 5, 7)
        if n % 10 == 0 or not is_truncatable_prime(n // 10):
            return False
        return is_truncatable_prime(n // 10)
    x = nums[54]
    return sorted((n for n in range(2, x + 1) if is_truncatable_prime(n)))