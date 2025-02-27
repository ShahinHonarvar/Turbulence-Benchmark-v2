def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    str_n = str(n)
    if '0' in str_n:
        return False
    left, right = (0, len(str_n) - 1)
    while left < right and is_prime(int(str_n[left:right + 1])):
        left += 1
        right -= 1
    return left >= right

def all_left_right_truncatable_prime(nums):
    x = nums[100]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)