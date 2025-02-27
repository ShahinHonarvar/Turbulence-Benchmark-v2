def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    n = str(n)
    for i in range(len(n)):
        if not is_prime(int(n[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[90]
    truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes