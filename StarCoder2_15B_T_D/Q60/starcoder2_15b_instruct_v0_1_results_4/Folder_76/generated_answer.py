def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = []
    for prime in generate_primes(x):
        if is_left_right_truncatable_prime(prime):
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_left_right_truncatable_prime(prime):
    if prime < 10:
        return False
    if str(prime).find('0') != -1:
        return False
    prime_str = str(prime)
    while len(prime_str) > 1:
        if not is_prime(int(prime_str)):
            return False
        prime_str = prime_str[1:]
        prime_str = prime_str[:-1]
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes