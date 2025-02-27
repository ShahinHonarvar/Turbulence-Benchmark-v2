from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[100]
    right_truncatable_primes = []
    for prime in (i for i in range(2, x) if isprime(i)):
        num_str = str(prime)
        while len(num_str) > 1 and isprime(int(num_str)):
            if len(num_str) == 1:
                right_truncatable_primes.append(prime)
            num_str = num_str[:-1]
    return sorted(right_truncatable_primes, reverse=True)