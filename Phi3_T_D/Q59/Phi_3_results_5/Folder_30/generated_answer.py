def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    if n not in primes:
        return False
    str_n = str(n)
    while str_n:
        str_n = str_n[1:]
        if not is_prime(int(str_n)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    primes = {p for p in range(2, x) if is_prime(p)}
    left_truncatables = [p for p in primes if is_left_truncatable_prime(p, primes)]
    left_truncatables.sort(reverse=True)
    return left_truncatables