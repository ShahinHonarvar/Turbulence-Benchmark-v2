def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    is_truncatable = True
    num_str = str(n)
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
            is_truncatable = False
            break
    return is_truncatable

def all_left_right_truncatable_prime(nums):
    x = nums[71]
    result = []
    for num in range(2, x + 1)[::-1]:
        if is_truncatable_prime(num):
            result.append(num)
    return result