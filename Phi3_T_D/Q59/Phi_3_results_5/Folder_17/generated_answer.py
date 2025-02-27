from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[36]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable = []
    for prime in primes:
        P = str(prime)
        if all((isprime(int(P[i:])) and '0' not in P[i:] for i in range(len(P)))):
            left_truncatable.append(prime)
    return sorted(left_truncatable, reverse=True)