def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    truncatable_primes = []
    for prime in primes_up_to(x):
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def primes_up_to(x):
    primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_truncatable_prime(prime):
    if prime < 10:
        return False
    if not is_prime(prime):
        return False
    while prime >= 10:
        prime = int(str(prime)[1:])
        if not is_prime(prime):
            return False
    while prime >= 10:
        prime = int(str(prime)[:-1])
        if not is_prime(prime):
            return False
    return True