def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[69]
    right_trunc_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)