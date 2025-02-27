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

def is_right_truncatable_prime(primal_prime, n):
    while n > 0:
        if not is_prime(primal_prime):
            return False
        n //= 10
        primal_prime = primal_prime % 10 ** (len(str(primal_prime)) - 1)
    return True

def all_right_truncatable_prime(tup):
    x = tup[100]
    left_truncatable_primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for prime in left_truncatable_primes:
        while is_right_truncatable_prime(prime * 10, 0):
            right_truncatable_primes.append(prime)
            prime = prime * 10 + 2
            if prime * 10 > x:
                break
    return sorted(set(right_truncatable_primes), reverse=True)