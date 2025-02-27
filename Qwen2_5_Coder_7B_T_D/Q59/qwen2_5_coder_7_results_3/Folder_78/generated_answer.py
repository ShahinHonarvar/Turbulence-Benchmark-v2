from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[23]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        all_primes = [int(str_prime[:i]) for i in range(1, len(str_prime) + 1)]
        if all((isprime(i) for i in all_primes)):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)