def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[0]
    left_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i)]
    right_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i)]
    for i in range(1, len(str(x))):
        left_truncatable_primes = [p for p in left_truncatable_primes if p // 10 ** i in left_truncatable_primes]
        right_truncatable_primes = [p for p in right_truncatable_primes if p % 10 ** (len(str(p)) - i) in right_truncatable_primes]
    return sorted(set(left_truncatable_primes) & set(right_truncatable_primes), reverse=True)