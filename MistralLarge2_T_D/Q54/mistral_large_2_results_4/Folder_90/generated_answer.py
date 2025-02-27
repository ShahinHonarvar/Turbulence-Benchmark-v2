def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[466]
    primes = [2, 3, 5, 7]
    rtp = []
    for p in primes:
        temp = p
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            rtp.append(p)
    for p in range(11, x):
        if not is_prime(p):
            continue
        temp = p
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            rtp.append(p)
    return sorted(rtp, reverse=True)