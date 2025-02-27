from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[64]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        is_left_truncatable = True
        for j in range(len(str_prime)):
            if not isprime(int(str_prime[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)