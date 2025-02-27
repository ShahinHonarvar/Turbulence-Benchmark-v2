def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_left_truncatable_prime(n, original=True):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return original

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)