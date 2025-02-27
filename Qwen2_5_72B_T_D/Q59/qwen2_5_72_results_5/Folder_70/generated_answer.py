def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[433]
    primes = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        if all((is_prime(int(s[i:])) for i in range(len(s)))):
            primes.append(num)
    return sorted(primes, reverse=True)