def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        s = str(n)
        for i in range(len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    x = nums[96]
    result = [n for n in range(10, x + 1) if '0' not in str(n) and is_lr_truncatable_prime(n)]
    return sorted(result, reverse=True)