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
    x = t[4]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        trunc = num
        while trunc:
            if not is_prime(trunc):
                break
            trunc = int(str(trunc)[1:]) if trunc > 9 else 0
        else:
            primes.append(num)
    return sorted(primes)