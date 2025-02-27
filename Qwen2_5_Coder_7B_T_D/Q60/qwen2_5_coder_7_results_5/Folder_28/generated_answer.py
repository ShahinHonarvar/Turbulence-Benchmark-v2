import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    primes = list(sympy.primerange(2, x + 1))
    left_right_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_truncatable = True
        for i in range(1, len(str_prime)):
            if not sympy.isprime(int(str_prime[i:])) or not sympy.isprime(int(str_prime[:-i])):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable.append(prime)
    return sorted(left_right_truncatable)