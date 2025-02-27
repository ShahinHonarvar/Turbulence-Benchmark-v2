from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    limit = x
    primes = []

    def is_left_truncatable(num):
        while num > 0:
            if '0' in str(num) or not isprime(num):
                return False
            num //= 10
        return True
    for num in range(2, limit):
        if str(num)[0] in '2357' and is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)