def is_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    while n > 9:
        n = int(str(n)[1:])
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for n in nums:
        if is_truncatable_prime(n):
            result.append(n)
    return result