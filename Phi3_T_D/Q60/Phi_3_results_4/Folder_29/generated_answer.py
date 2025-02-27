def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[1:-1]
    return True

def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[55]
    truncatable_primes = []
    for prime in range(2, x + 1):
        if is_left_and_right_truncatable(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)