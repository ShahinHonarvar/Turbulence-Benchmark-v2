def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[945]

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        if not is_prime(n):
            return False
        return is_truncatable_prime(n // 10)
    result = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

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