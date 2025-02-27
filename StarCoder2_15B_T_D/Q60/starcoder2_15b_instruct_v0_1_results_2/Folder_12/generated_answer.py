import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    truncatable_primes = []
    for i in range(10, x + 1):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)