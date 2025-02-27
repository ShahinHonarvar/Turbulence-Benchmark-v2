def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not n:
        return False
    return all((is_prime(n[1:i]) for i in range(2, len(str(n)) + 1))) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[54]
    if x < 11:
        return []
    return [i for i in range(x, 1, -1) if is_left_right_truncatable_prime(i)]