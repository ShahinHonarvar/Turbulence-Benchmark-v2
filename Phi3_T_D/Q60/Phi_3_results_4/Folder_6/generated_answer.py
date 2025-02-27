from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[74]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if all((isprime(int(str_prime[i:])) and isprime(int(str_prime[:len(str_prime) - i])) for i in range(1, len(str_prime) // 2))):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)