def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatable_primes = []
    for prime in primes_less_than(x):
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_left_truncatable_prime(prime):
    if '0' in str(prime):
        return False
    for i in range(1, len(str(prime))):
        truncated_prime = int(str(prime)[i:])
        if not is_prime(truncated_prime):
            return False
    return True

def primes_less_than(x):
    pass

def is_prime(n):
    pass