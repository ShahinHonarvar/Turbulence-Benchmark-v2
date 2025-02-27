def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[23]

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))
    return sorted([n for n in range(1, x + 1) if is_left_right_truncatable_prime(n)])