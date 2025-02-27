from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    primes = []

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)