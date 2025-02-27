from sympy import primerange

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = list(primerange(1, x + 1))
    truncatable_primes = []
    for prime in primes:
        prime_str = str(prime)
        if '0' in prime_str:
            continue
        if all((int(prime_str[:i]) in primes for i in range(1, len(prime_str)))):
            if all((int(prime_str[-i:]) in primes for i in range(1, len(prime_str)))):
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)