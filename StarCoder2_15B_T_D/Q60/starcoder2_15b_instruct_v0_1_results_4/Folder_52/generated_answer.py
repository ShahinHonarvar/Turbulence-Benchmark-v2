import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    truncatable_primes = []
    for i in range(2, x + 1):
        if not is_prime(i):
            continue
        truncatable = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:len(str(i)) - j])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes