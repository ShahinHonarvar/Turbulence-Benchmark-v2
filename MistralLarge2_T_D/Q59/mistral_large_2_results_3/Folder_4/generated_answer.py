def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[96]
    primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)