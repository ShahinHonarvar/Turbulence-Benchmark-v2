def is_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    for i in range(len(num_str) - 1, -1, -1):
        if not is_prime(int(num_str[:i + 1])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)