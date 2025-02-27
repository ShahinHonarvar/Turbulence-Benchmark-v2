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

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    num = n
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)