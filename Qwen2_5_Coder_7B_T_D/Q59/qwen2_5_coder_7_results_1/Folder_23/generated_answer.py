from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[77]
    primes_less_than_x = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes_less_than_x:
        str_prime = str(prime)
        if '0' not in str_prime:
            is_left_truncatable = True
            for i in range(len(str_prime)):
                if not isprime(int(str_prime[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)