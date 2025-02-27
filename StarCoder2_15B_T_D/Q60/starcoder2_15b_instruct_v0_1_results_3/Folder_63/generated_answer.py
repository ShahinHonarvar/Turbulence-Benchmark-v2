def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = []
    for prime in primes_up_to(x):
        if is_left_right_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_left_right_truncatable_prime(prime):
    if prime < 10:
        return False
    if prime in [2, 3, 5, 7]:
        return True
    prime_str = str(prime)
    for i in range(len(prime_str)):
        if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:len(prime_str) - i])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes