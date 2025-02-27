def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    return [n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n)]