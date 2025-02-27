import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[97]
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            truncatable = True
            num_str = str(i)
            while len(num_str) >= 2:
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
                num_str = num_str[1:]
            if truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes