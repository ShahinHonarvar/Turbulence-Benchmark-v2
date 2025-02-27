from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[85]
    left_primes = []

    def is_left_truncatable(prime):
        for i in range(len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable(num):
            left_primes.append(num)
    return left_primes