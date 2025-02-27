def all_left_truncatable_prime(nums):
    left_truncatable = []
    for num in nums:
        if num < 10 and is_prime(num):
            left_truncatable.append(num)
    left_truncatable.sort()
    return left_truncatable

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True