def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(nums):
    x = nums[835]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for p in primes:
        while p:
            if not is_prime(int(p)):
                break
            right_truncatable_primes.append(int(p))
            p = p[:-1]
    return sorted(right_truncatable_primes)