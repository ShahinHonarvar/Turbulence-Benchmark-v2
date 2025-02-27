import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[126]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if is_prime(num):
            truncated = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    truncated = False
                    break
            if truncated:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)