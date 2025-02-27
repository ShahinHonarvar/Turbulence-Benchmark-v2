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

def all_left_truncatable_prime(t):
    x = t[85]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0
        return True
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)