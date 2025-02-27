def is_left_right_truncatable_prime(n, primes):
    if n < 2:
        return False
    if len(str(n)) == 1:
        return True
    return all((str(n)[i:] in primes and str(n)[:-i] in primes for i in range(1, len(str(n)))))

def find_primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if all((i % p for p in primes)):
            primes.append(i)
    return primes

def all_left_right_truncatable_prime(numbers_tuple):
    primes = find_primes_up_to(numbers_tuple[630])
    left_right_primes = [p for p in primes if is_left_right_truncatable_prime(p, primes)]
    return sorted(left_right_primes, reverse=True)