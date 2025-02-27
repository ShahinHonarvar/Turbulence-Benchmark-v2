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

def is_truncatable(n):
    n = str(n)
    if len(n) == 1 or len(n) == 2:
        return is_prime(int(n))
    if not is_prime(int(n)):
        return False
    for i in range(1, len(n)):
        if not (is_prime(int(n[i:])) and is_prime(int(n[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[81]
    return sorted(filter(is_truncatable, range(2, x + 1)), reverse=True)