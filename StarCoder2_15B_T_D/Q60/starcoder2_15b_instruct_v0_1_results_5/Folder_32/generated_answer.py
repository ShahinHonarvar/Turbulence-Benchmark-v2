def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[42]

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        return is_truncatable_prime(int(str(n)[1:])) and is_truncatable_prime(int(str(n)[:-1]))
    return sorted((n for n in range(2, x + 1) if is_truncatable_prime(n)))