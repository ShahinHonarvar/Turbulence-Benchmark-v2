def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[93]

    def is_left_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        d = len(str(n))
        return is_prime(n // 10 ** (d - 1)) and is_prime(n % 10)
    return [i for i in range(2, x + 1) if is_left_right_truncatable(i)]