import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    left_truncatable_primes = []
    for i in range(2, x):
        number = i
        while number > 0:
            if not is_prime(number):
                break
            number //= 10
        if number == 0:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)