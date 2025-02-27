import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_right_prime(n, d):
    if not is_prime(n):
        return False
    if len(str(n)) == 1:
        return True
    return is_truncatable_right_prime(int(str(n)[:-1]), d + 1)

def all_right_truncatable_prime(numbers):
    x = numbers[644]
    if x <= 1:
        return []
    right_truncatables = set()
    for i in range(2, x):
        if all((is_prime(int(str(i)[:j + 1])) for j in range(len(str(i))))) and is_truncatable_right_prime(i, 0):
            right_truncatables.add(i)
    return sorted(list(right_truncatables))