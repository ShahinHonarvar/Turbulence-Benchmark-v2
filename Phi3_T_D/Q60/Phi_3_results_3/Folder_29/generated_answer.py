def is_truncatable_prime(n):
    if n < 10:
        return n in (2, 3, 5, 7)
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 100 // 10
        if n == 0:
            return False
    return True

def all_left_right_truncatable_prime(integers):
    x = integers[55]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True