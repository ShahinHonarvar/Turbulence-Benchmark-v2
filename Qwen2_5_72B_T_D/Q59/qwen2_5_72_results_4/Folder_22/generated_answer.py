def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[85]
    truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        is_truncatable = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes