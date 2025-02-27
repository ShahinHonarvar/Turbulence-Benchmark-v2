def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for prime in numbers:
        if is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(prime):
    if not is_prime(prime):
        return False
    while prime > 0:
        prime //= 10
        if not is_prime(prime):
            return False
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True