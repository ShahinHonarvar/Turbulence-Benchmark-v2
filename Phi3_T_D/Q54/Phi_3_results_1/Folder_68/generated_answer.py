def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    primes = [2, 3, 5, 7]
    right_truncatable = []
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 2
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 3
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 4
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 5
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 6
    for prime in primes:
        while prime < n:
            if is_prime(prime):
                right_truncatable.append(prime)
            prime = prime * 10 + 7
    return sorted(set(right_truncatable), reverse=True)

def all_right_truncatable_prime(numbers):
    x = numbers[1]
    if not isinstance(x, int) or x <= 0:
        return []
    return right_truncatable_primes(x)