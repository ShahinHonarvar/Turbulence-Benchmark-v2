from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    primes = []

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable(num):
            primes.append(num)
    return primes