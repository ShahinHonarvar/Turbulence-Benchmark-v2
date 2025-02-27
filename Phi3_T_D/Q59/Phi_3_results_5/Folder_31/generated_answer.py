def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    truncatable_primes = []
    for prime in filter(is_prime, range(23, n)):
        str_prime = str(prime)
        if all((is_prime(int(str_prime[i:])) for i in range(len(str_prime)))):
            truncatable_primes.append(prime)
    return truncatable_primes

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    return sorted(left_truncatable_primes(x), reverse=True)