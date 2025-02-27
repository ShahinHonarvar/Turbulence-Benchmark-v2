from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    limit = x - 1
    primes = [i for i in range(2, limit) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if all((isprime(int(str_prime[:i])) for i in range(1, len(str_prime)))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)