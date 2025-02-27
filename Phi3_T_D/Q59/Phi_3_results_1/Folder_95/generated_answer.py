from sympy import isprime, primerange

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []
    for prime in primerange(11, x):
        if '0' not in str(prime):
            prime_str = str(prime)
            can_truncate = True
            for i in range(len(prime_str)):
                truncated_number = int(prime_str[i:])
                if not isprime(truncated_number):
                    can_truncate = False
                    break
            if can_truncate:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)