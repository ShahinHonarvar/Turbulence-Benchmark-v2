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
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = nums[992]
    result = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if '0' not in str(num) and is_prime(num) and is_lr_truncatable_prime(num):
            result.append(num)
    return result