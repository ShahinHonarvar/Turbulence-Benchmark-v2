from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[74]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        num = n
        while num > 0:
            if '0' in str(num) or not isprime(num):
                return False
            num = num // 10
        return True
    for num in range(2, x):
        if '0' not in str(num) and isprime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)