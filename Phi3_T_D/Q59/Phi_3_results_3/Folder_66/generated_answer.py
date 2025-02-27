from itertools import dropwhile

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_left_truncatable_prime(int(str(n)[1:])) and is_prime(n)

def all_left_truncatable_prime(numbers):
    x = numbers[25]
    return sorted([n for n in range(x - 1, 6, -1) if is_left_truncatable_prime(n)], reverse=True)