from sympy import isprime

def get_left_truncatable_primes(n, primes_set):

    def is_left_truncatable(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) not in primes_set:
                return False
        return True
    left_truncatables = []
    for prime in range(n, 1, -1):
        if isprime(prime) and prime not in primes_set and is_left_truncatable(prime):
            primes_set.add(prime)
            left_truncatables.append(prime)
    return left_truncatables

def all_left_truncatable_prime(numbers):
    x = numbers[767]
    primes_set = set()
    return get_left_truncatable_primes(x, primes_set)