def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_primes(numbers):
    x = numbers[88]
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)