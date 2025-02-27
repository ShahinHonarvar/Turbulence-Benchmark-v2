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

def all_left_right_truncatable_prime(t):
    x = t[91]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for p in primes:
        s = str(p)
        if '0' in s:
            continue
        left, right = (s, s)
        while len(left) > 1 and len(right) > 1:
            left = left[1:]
            right = right[:-1]
            if not (is_prime(int(left)) and is_prime(int(right))):
                break
        else:
            if is_prime(int(left)) and is_prime(int(right)):
                truncatable_primes.append(p)
    return sorted(truncatable_primes)