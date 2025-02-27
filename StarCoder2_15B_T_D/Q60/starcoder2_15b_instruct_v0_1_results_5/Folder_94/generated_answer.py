def all_left_right_truncatable_prime(x):
    return [prime for prime in range(2, x + 1) if is_left_right_truncatable_prime(prime)]

def is_left_right_truncatable_prime(prime):
    if prime < 10:
        return is_prime(prime)
    if not is_prime(prime):
        return False
    return is_left_right_truncatable_prime(int(str(prime)[1:])) and is_left_right_truncatable_prime(int(str(prime)[:-1]))

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