def all_left_right_truncatable_prime(nums):
    x = nums[28]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if str(n).count('0') == 0 and is_truncatable_prime(n)])