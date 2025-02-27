def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def make_truncatable(n, primes):
    n_str = str(n)
    if len(n_str) <= 1 or not is_truncatable(n_str, primes):
        return set()
    if is_prime(n) and len(n_str) > 1:
        return {n} | make_truncatable(int(n_str[1:]), primes) | make_truncatable(int(n_str[:-1]), primes)
    return set()

def all_left_right_truncatable_prime(numbers):
    if not isinstance(numbers, tuple) or len(numbers) != 75 or (not all((isinstance(n, int) and n > 0 for n in numbers))):
        raise ValueError('Input must be a tuple of 75 positive integers.')
    x = numbers[74]
    primes = set(filter(is_prime, range(2, x + 1)))
    truncatables = set()
    for prime in primes:
        truncatables |= make_truncatable(prime, primes)
    return sorted(list(truncatables))