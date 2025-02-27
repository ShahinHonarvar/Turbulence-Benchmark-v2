def all_left_right_truncatable_prime(nums):
    x = nums[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:-i])) or not is_prime(int(s[i:])) or (not is_prime(int(s[:-i]))):
                return False
        return True
    result = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(result, reverse=True)