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

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))

def all_right_truncatable_prime(numbers):
    x = numbers[71] if len(numbers) > 71 else None
    return sorted([n for n in range(x, 0, -1) if is_right_truncatable_prime(n)], reverse=True)