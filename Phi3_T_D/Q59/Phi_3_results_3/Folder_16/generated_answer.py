def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[792]
    left_truncatable_primes = []
    no_zero_primes = [p for p in range(2, x) if '0' not in str(p) and is_prime(p)]
    for prime in no_zero_primes:
        prime_str = str(prime)
        if all((is_prime(int(prime_str[i:])) for i in range(1, len(prime_str)))):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes