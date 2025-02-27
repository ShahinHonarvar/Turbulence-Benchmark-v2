from sympy import isprime, primerange

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    right_truncatable_primes = []
    for prime in primerange(10, x):
        str_prime = str(prime)
        is_right_truncatable = True
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[:i + 1])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)