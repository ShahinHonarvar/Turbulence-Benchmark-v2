from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for prime in primes:
        if prime < x:
            left_truncatable_primes.append(prime)
            truncated_prime = prime // 10
            while truncated_prime > 0 and isprime(truncated_prime):
                left_truncatable_primes.append(truncated_prime)
                truncated_prime //= 10
    return sorted(left_truncatable_primes, reverse=True)