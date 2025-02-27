import math

def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return is_prime(n)
    x = nums[50]
    result = [i for i in range(10, x) if is_left_truncatable(i)]
    return sorted(result, reverse=True)