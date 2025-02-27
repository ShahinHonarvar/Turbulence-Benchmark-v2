def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_chain(n, primes):
    if n < 10 or not is_prime(n):
        return primes
    next_num = n % 10
    if n // 10 == 0:
        return primes
    next_trunc_chain = left_truncatable_chain(n // 10, primes + [n])
    return next_trunc_chain

def all_left_truncatable_prime(numbers):
    x = numbers[466]
    primes = [p for p in range(2, x) if is_prime(p)]
    left_trunc_primes = []
    for prime in primes:
        chain = left_truncatable_chain(prime, [])
        if prime in chain:
            left_trunc_primes.extend(chain)
    return sorted(left_trunc_primes, reverse=True)