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

def is_truncatable_prime(n):
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])) or not is_prime(int(n[:i])):
            return False
    return len(n) > 1

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)