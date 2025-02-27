def all_left_truncatable_prime(nums):
    x = nums[630]

    def is_left_truncatable_prime(num):
        if num < 10:
            return False
        if not is_prime(num):
            return False
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        return True
    res = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(res, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True