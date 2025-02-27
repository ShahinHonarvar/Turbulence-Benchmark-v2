def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        if '0' in str(n) or not is_prime(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not is_prime(int(s)):
                return False
        return True
    x = nums[22]
    result = [i for i in range(10, x + 1) if is_lr_truncatable_prime(i)]
    return sorted(result, reverse=True)