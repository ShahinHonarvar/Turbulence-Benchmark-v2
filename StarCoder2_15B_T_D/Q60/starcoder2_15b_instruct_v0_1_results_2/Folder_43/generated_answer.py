import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    truncatable_primes = []
    for i in range(10, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:len(str(i)) - j])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes