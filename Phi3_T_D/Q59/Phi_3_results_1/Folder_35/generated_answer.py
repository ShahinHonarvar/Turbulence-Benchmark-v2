def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    max_value = tup[177]
    left_truncatable_primes = []
    for prime in range(2, max_value):
        if is_prime(prime):
            str_prime = str(prime)
            if all((is_prime(int(str_prime[i:])) for i in range(len(str_prime)))):
                left_truncatable_primes.append(prime)
    return left_truncatable_primes