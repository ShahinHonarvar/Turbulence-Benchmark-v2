from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_left_truncatable = True
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)