def all_right_truncatable_prime(numbers):
    x = numbers[39]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            if is_right_truncatable_prime(i):
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n >= 10:
        n //= 10
        if not is_prime(n):
            return False
    return True