from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[125]
    right_truncatable_primes = {i for i in range(23, x) if isprime(i)}
    result = []
    for prime in reversed(sorted(right_truncatable_primes)):
        prime_str = str(prime)
        while prime > 0:
            if isprime(int(prime_str)):
                result.append(prime)
                break
            prime = int(prime_str[:-1])
            prime_str = str(prime)
    return sorted(result, reverse=True)