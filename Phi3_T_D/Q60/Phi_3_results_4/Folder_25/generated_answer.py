def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    rotation_str = str(n)
    length = len(rotation_str)
    for i in range(length):
        left = int(rotation_str[i:])
        right = int(rotation_str[:length - i])
        if left < 10 and right < 10:
            return False
        if not is_prime(left) or left not in primes:
            return False
        if right < 10 and (not is_prime(right)):
            return False
        if right >= 10 and right not in primes:
            return False
    return True

def generate_primes(limit):
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = generate_primes(x)
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime, primes):
            truncatable_primes.append(prime)
    return truncatable_primes