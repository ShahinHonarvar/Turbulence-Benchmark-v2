def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    if not (is_prime(n) and str(n).strip('0')):
        return False
    left_truncable = all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))))
    right_truncable = all((is_prime(int(str(n)[-i:])) for i in range(1, len(str(n)) + 1)))
    return left_truncable and right_truncable

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    return sorted(filter(is_left_and_right_truncatable, range(2, x + 1)), reverse=True)