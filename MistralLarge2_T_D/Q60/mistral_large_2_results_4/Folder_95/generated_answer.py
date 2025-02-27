def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_right_truncatable_prime(num):
    if not is_prime(num) or '0' in str(num):
        return False
    str_num = str(num)
    left, right = (0, len(str_num) - 1)
    while left < right:
        if not is_prime(int(str_num[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[77]
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes)