def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, primes):
    str_n = str(n)
    return all((is_prime(int(str_n[:-i])) and int(str_n[:-i]) in primes for i in range(1, len(str_n))))

def all_right_truncatable_prime(int_tuple):
    x = int_tuple[39]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([prime for prime in primes if is_truncatable(prime, primes)], reverse=True)