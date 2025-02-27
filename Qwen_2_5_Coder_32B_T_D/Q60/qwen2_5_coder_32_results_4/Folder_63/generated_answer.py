def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:-i])) for i in range(len(str_n) - 1))) if len(str_n) > 2 else True
    x = nums[88]
    result = [n for n in range(2, x + 1) if '0' not in str(n) and is_prime(n) and is_left_right_truncatable(n)]
    return result