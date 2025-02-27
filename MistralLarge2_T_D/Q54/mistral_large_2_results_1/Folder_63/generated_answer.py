def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes():
    primes = [2, 3, 5, 7]
    for prime in primes:
        yield prime
    while primes:
        prime = primes.pop(0)
        for digit in '1379':
            new_prime = int(str(prime) + digit)
            if is_prime(new_prime):
                primes.append(new_prime)
                yield new_prime

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_prime_numbers = list(right_truncatable_primes())
    return sorted([p for p in right_truncatable_prime_numbers if p < x])