import re

def all_right_truncatable_prime(arg):
    x = arg[79]
    truncatable_primes = []
    for n in range(2, x):
        if is_prime(n):
            digits = [int(d) for d in str(n)]
            for i in range(len(digits) - 1):
                if not is_prime(int(''.join(map(str, digits[i:])))):
                    break
            else:
                truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True