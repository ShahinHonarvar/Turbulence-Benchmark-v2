def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def generate_primes_up_to(x):
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, x + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, x + 1, i):
                sieve[j] = False
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    prime_numbers = generate_primes_up_to(x)
    left_truncatable_primes = [p for p in prime_numbers if is_left_truncatable(p, prime_numbers)]
    return left_truncatable_primes