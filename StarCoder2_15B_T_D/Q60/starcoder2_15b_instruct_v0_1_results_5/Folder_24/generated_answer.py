def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    x65 = x[65]

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))
    return sorted((n for n in range(2, x65 + 1) if is_truncatable_prime(n)), reverse=True)