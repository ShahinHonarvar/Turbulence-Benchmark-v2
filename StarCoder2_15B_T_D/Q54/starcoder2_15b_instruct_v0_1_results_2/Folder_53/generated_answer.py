from math import log10

def all_right_truncatable_prime(nums):
    x = nums[86]
    upper_bound = int(log10(x))
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable_prime = True
        for j in range(1, upper_bound + 1):
            truncated_num = i // 10 ** j
            if not is_prime(truncated_num):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True