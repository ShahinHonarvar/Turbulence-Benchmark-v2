def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    if not is_prime(n):
        return False
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[52]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)