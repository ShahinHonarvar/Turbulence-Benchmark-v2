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

def is_truncatable_prime(n):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[38]
    while True:
        if is_prime(x) and is_truncatable_prime(x):
            return sorted([i for i in range(x + 1, 0, -1) if is_prime(i) and is_truncatable_prime(i)], reverse=True)
        x -= 1