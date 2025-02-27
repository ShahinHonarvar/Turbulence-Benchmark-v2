def is_left_right_truncatable_prime(n):
    if n < 10:
        return True
    if '0' in str(n) or not is_prime(n):
        return False
    return all((is_left_right_truncatable_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    if not is_prime(x):
        return []
    return sorted(filter(is_left_right_truncatable_prime, range(2, x + 1)), reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True