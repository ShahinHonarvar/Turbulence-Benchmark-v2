def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    primes = []
    for i in range(23, input_tuple[11]):
        if is_truncatable(i, primes):
            primes.append(i)
    return primes