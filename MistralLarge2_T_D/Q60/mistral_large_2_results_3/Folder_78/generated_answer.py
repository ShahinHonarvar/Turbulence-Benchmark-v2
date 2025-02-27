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
    x = t[23]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            n = str(num)
            if '0' in n:
                continue
            while len(n) > 1 and is_prime(int(n)):
                n = n[1:-1]
            if len(n) > 0 and is_prime(int(n)):
                primes.append(num)
    return sorted(primes)