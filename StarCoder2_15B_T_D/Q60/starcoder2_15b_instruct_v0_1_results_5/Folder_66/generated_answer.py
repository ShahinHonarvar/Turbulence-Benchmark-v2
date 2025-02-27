from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[25]
    truncatable_primes = []
    for i in range(1, x + 1):
        if '0' in str(i) or not is_prime(i):
            continue
        truncatable = True
        for j in range(1, len(str(i))):
            left = int(str(i)[j:])
            right = int(str(i)[:-j])
            if not is_prime(left) or not is_prime(right):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes