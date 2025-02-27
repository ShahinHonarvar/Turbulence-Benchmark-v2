def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(pr):
    if pr < 10:
        return is_prime(pr)
    return pr % 10 != 0 and is_left_right_truncatable_prime(pr // 10) and is_prime(int(str(pr)[:-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])