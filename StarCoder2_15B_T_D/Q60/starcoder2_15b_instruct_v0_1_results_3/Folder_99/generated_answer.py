import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_prime(num):
            digits = str(num)
            for i in range(len(digits)):
                if not is_prime(int(digits[i:])) or not is_prime(int(digits[:len(digits) - i])):
                    break
            else:
                result.append(num)
    return result