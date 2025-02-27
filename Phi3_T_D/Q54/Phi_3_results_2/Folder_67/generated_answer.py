def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(nums):
    x = nums[71]
    primes = {p for p in range(2, x) if is_prime(p)}
    right_truncs = {p for p in primes if all((is_prime(int(str(p)[:i + 1])) for i in range(len(str(p)))))}
    return sorted(list(right_truncs), reverse=True)