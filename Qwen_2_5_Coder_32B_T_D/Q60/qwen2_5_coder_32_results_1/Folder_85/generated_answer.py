def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[94]
    lr_trunc_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        is_lr_trunc_prime = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                is_lr_trunc_prime = False
                break
        if is_lr_trunc_prime and is_prime(num):
            lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes)