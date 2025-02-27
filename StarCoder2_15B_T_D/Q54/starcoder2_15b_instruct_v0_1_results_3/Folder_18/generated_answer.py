import math

def all_right_truncatable_prime(nums):
    x = nums[429]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        for i in range(len(str(num)) - 1):
            truncated_num = int(str(num)[:len(str(num)) - i - 1])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True