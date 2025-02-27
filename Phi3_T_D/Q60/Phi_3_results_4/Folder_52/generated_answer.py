def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_right_truncatable(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    return len(str_n) > 1 and all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(1, len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    return sorted([n for n in range(2, x + 1) if left_right_truncatable(n)], reverse=True)