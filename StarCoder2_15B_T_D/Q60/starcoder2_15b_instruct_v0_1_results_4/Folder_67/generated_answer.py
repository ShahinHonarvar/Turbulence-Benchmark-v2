def is_truncatable_prime(num):
    num_str = str(num)
    if num_str.find('0') != -1:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
        if not is_prime(int(num_str[:len(num_str) - i])):
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
    x = nums[71]
    for num in range(1, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result