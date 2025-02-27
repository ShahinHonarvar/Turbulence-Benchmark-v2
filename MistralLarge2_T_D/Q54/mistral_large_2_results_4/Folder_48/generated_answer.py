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

def right_truncatable_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp != 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            truncatable_primes.append(prime)
    return truncatable_primes

def all_right_truncatable_prime(t):
    x = t[835]
    return sorted(right_truncatable_primes(x))