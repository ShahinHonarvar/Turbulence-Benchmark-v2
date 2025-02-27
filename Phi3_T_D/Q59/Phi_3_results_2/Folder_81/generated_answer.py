from itertools import product

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers, index):
    x = numbers[index]
    left_truncatable_primes = []
    for i in range(2, x):
        n = i
        while n > 0:
            if not is_prime(n):
                break
            n = n // 10
        if n == 0:
            left_truncatable_primes.append(i)
    return left_truncatable_primes