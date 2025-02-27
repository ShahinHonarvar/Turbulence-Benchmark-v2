import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    right_truncatable_primes = []
    for num in range(10, x):
        if is_prime(num):
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)