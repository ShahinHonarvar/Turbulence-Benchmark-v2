import math

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    is_right_truncatable_prime = [False] * x
    for i in range(2, x):
        if is_right_truncatable_prime[i]:
            continue
        if not is_prime(i):
            is_right_truncatable_prime[i] = False
            continue
        is_right_truncatable_prime[i] = True
        j = i * 2
        while j < x:
            is_right_truncatable_prime[j] = False
            j += i
    return sorted([i for i in range(2, x) if is_right_truncatable_prime[i]])

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True