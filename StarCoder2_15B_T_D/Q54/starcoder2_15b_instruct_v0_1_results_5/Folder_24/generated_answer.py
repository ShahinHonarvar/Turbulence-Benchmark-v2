def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[65]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(len(str(i)) - 1, 0, -1):
            truncated_num = int(str(i)[:j])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)