def all_left_right_truncatable_prime(tuple_of_pos_ints):
    x = tuple_of_pos_ints[429]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n):
        return False
    return is_left_right_truncatable_prime(n // 10)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True