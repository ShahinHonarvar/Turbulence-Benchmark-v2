def is_prime(n):
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    return all((n % d for d in range(3, int(n ** 0.5) + 1, 2)))

def left_truncatable_primes(threshold):
    primes = [str(p) for p in range(11, threshold) if is_prime(p)]
    valid_primes = [int(p) for p in primes if all((is_prime(int(p[:i])) for i in range(1, len(p))))]
    valid_primes.sort(reverse=True)
    return valid_primes

def all_left_truncatable_prime(int_tuple):
    x = int(int_tuple[96])
    return left_truncatable_primes(x)