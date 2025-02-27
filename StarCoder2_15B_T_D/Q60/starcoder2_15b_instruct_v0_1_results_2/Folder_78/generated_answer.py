def all_left_right_truncatable_prime(args):
    left_right_truncatable_primes = []
    for prime in args:
        if is_left_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(prime):
    if prime < 10:
        return is_prime(prime)
    if prime % 10 == 0:
        return False
    if not is_prime(prime):
        return False
    return is_left_right_truncatable_prime(prime // 10)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True