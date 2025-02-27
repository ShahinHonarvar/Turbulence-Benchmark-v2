from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[67]
    limit = int(x ** 0.5)
    primes = [i for i in range(2, limit + 1) if isprime(i)]
    left_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if '0' in str_prime:
            continue
        if all((isprime(int(str_prime[:i])) for i in range(1, len(str_prime)))):
            left_truncatable.append(prime)
    return sorted(left_truncatable, reverse=True)