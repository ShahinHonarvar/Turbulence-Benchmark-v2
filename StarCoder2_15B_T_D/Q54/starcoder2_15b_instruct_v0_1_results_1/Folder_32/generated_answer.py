def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[42]
    result = []
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(i):
            result.append(i)
    return sorted(result)