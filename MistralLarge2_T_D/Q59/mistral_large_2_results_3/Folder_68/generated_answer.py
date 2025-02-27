def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[1]
    primes = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        while s:
            if not is_prime(int(s)):
                break
            s = s[1:]
        else:
            primes.append(num)
    return sorted(primes, reverse=True)