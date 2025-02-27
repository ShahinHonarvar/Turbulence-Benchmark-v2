def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[49]
    result = []
    for i in range(1, x):
        num = i
        while num < x:
            if not is_prime(num):
                break
            num //= 10
        if num == 0:
            result.append(i)
    return sorted(result)