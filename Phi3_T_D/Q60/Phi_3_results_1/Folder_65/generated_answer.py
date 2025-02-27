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

def all_left_right_truncatable_prime(numbers):
    x = numbers[32] if len(numbers) > 32 else None
    if x is None or not isinstance(x, int) or x < 1:
        return []

    def is_left_right_truncatable(num):
        s = str(num)
        for i in range(1, len(s) // 2 + 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])