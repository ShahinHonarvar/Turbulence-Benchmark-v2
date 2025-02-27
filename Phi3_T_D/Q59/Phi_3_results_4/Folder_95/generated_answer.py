def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, prime_set):
    while n > 0:
        if not is_prime(n) or n == 0:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    max_x = numbers[77]
    primes = set()
    left_truncatable_primes = []
    for number in range(2, max_x):
        if is_prime(number):
            primes.add(number)
    for prime in primes:
        if is_left_truncatable(prime, primes):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes