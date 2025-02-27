def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[77]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        s = str(prime)
        if '0' in s:
            continue
        while len(s) > 1:
            s = s[1:-1]
            if not is_prime(int(s)):
                break
            if len(s) <= 2 and is_prime(int(s)):
                truncatable_primes.append(prime)
                break
    return sorted(truncatable_primes, reverse=True)