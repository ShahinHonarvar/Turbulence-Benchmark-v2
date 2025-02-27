def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if not is_prime(num):
        return False
    s = str(num)
    if '0' in s:
        return False
    while len(s) > 1:
        s = s[1:]
        if not is_prime(int(s)):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[784]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)