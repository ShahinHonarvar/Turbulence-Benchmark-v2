def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        last_digit = num % 10
        if last_digit in (2, 4, 5, 6, 8, 0):
            return False
        return is_right_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[91]
    result = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)