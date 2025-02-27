from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[10]
    primes = [n for n in range(2, x + 1) if isprime(n) and '0' not in str(n)]
    lr_primes = []
    for p in primes:
        s = str(p)
        while len(s) > 1:
            if not isprime(int(s)):
                break
            s = s[1:-1]
        else:
            if isprime(int(s)):
                lr_primes.append(p)
    return sorted(lr_primes, reverse=True)