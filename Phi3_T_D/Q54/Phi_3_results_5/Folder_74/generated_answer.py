def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = []
    for num in range(2, x):
        if is_truncatable_prime(num):
            primes.append(num)
    primes.sort()
    return primes