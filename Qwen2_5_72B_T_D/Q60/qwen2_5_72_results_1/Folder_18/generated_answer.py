def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    return [n for n in range(x, 1, -1) if is_truncatable_prime(n)]