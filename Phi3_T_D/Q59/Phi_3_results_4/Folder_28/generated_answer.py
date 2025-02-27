def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if not n or '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []
    for number in range(2, x):
        if is_left_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes