from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[100]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    for num in range(2, x):
        if isleft_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)