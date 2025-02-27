def is_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)