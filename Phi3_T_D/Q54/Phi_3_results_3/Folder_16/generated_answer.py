def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    return n > 0 and is_prime(n) and all((is_prime(int(str(n)[:k])) for k in range(len(str(n)), 0, -1)))

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    return sorted((n for n in range(2, x) if is_right_truncatable_prime(n)))