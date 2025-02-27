def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[433]

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        if num < 10:
            return True
        return is_left_truncatable_prime(int(str(num)[1:]))
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)