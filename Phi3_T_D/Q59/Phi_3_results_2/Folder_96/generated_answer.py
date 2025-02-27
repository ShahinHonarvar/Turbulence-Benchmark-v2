def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, digits):
    if not is_prime(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    left_truncatable_primes = []
    for num in range(10, x, 2):
        if is_left_truncatable_prime(num, len(str(num))):
            left_truncatable_primes.append(num)
    return left_truncatable_primes