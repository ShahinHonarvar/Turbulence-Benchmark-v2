from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        for i in range(len(str(n))):
            if str(n)[i] == '0' or not isprime(int(str(n)[i:])):
                return False
        return True
    for num in range(2, x):
        if str(num)[0] == '0':
            continue
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)