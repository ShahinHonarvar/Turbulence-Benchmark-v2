def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n:
        n = n % 10 ** (len(str(n)) - 1)
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[31]
    primes = [i for i in range(2, x) if is_prime(i) and is_ltruncatable_prime(i)]
    return sorted(primes, reverse=True)