from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    primes = set()
    num = numbers[850]
    while num % 2 == 0:
        primes.add(2)
        num //= 2
    for i in range(3, int(sqrt(num)) + 1, 2):
        while num % i == 0:
            if is_prime(i):
                primes.add(i)
            num //= i
    if num > 2 and is_prime(num):
        primes.add(num)
    return primes if 850 < len(numbers) else None