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

def is_right_truncatable_prime(n):
    divisor = 10
    while n > 0:
        if not is_prime(n % divisor):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    right_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return right_truncatable_primes