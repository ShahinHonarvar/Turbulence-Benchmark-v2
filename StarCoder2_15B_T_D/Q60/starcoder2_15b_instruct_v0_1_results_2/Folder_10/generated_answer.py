def is_truncatable(num):
    if num < 10:
        return False
    num_str = str(num)
    for i in range(len(num_str)):
        truncated_num = int(num_str[i + 1:]) if i == 0 else int(num_str[:i] + num_str[i + 1:])
        if not is_prime(truncated_num):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)