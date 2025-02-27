def all_left_right_truncatable_prime(t):
    return [x for x in t if x <= t[175] and is_left_right_truncatable_prime(x)]

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True