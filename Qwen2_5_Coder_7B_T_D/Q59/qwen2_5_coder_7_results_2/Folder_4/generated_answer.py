from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = [2, 3, 5, 7]
    result = []

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n) or '0' in str(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable_prime(num):
            primes.append(num)
            result.append(num)
    result.sort(reverse=True)
    return result