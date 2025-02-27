def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes_set):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes_set = {2, 3, 5, 7}
    for i in range(10, x, 2):
        if all((i % p != 0 for p in primes_set)):
            primes_set.add(i)
    return sorted([p for p in primes_set if is_left_truncatable_prime(p, primes_set)])