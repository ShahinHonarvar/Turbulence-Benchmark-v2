def all_left_truncatable_prime(tup):
    x = tup[177]
    return sorted(left_truncatable_primes(x))

def left_truncatable_primes(x):
    primes = []
    for i in range(2, x):
        if is_prime(i):
            if is_left_truncatable_prime(i):
                primes.append(i)
    return primes

def is_left_truncatable_prime(n):
    if is_prime(n):
        if n < 10:
            return True
        else:
            return is_left_truncatable_prime(int(str(n)[1:]))
    else:
        return False

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True