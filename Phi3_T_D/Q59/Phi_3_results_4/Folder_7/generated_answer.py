def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    sieve = [True] * x
    for i in range(2, x):
        if sieve[i]:
            for j in range(i * 2, x, i):
                sieve[j] = False
    result = []
    for i in range(2, x):
        if sieve[i] and is_left_truncatable_prime(i, sieve):
            result.append(i)
    return result