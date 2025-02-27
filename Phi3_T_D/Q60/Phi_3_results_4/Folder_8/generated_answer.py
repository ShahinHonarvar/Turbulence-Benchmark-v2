def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    s = str(n)
    if len(s) == 1:
        return is_prime(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[41]
    return sorted([p for p in range(2, x + 1) if is_left_right_truncatable(p)], reverse=True)