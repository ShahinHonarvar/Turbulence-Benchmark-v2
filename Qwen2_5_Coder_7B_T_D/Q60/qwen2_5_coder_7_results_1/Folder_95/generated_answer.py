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

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:len(num_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[77]
    return sorted(filter(left_right_truncatable_prime, range(2, x + 1)))