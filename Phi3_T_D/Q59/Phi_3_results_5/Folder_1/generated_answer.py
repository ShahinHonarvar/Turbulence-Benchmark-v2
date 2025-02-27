from sympy import isprime

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[20]
    primes = [i for i in range(2, x) if isprime(i)]
    truncatables = []

    def is_left_truncatable(prime):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])):
                return False
        return True
    for p in primes:
        if is_left_truncatable(p):
            truncatables.append(p)
    return sorted(truncatables, reverse=True)