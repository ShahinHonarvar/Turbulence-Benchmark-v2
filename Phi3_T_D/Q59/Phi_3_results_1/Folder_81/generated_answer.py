def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, prime_len):
    number_str = str(n)
    for i in range(prime_len):
        if not is_prime(int(number_str[i:])):
            return False
    return True

def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n):
        if is_prime(possiblePrime):
            primes.append(possiblePrime)
    return primes

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[98]
    primes = generate_primes(x)
    left_truncatable_primes = [p for p in primes if len(str(p)) > 1 and is_left_truncatable_prime(p, len(str(p)))]
    return sorted(left_truncatable_primes)