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

def all_right_truncatable_prime(primes_tuple):
    x = primes_tuple[94]
    right_truncatable_primes = []
    for prime in range(2, x):
        str_prime = str(prime)
        while len(str_prime) > 1:
            if not is_prime(int(str_prime)):
                break
            str_prime = str_prime[:-1]
        if len(str_prime) == 1 and is_prime(int(str_prime)):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)