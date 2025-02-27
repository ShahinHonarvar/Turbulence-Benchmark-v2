from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    for num in range(2, x):
        if '0' not in str(num) and isprime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)