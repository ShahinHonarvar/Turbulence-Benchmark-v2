def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s) - 1):
            if not (is_prime(int(s[i + 1:])) and is_prime(int(s[:-i - 1]))):
                return False
        return True
    x = nums[57]
    result = [n for n in range(11, x + 1) if is_left_right_truncatable(n)]
    return sorted(result, reverse=True)