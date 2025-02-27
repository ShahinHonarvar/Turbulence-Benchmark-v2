def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    if not all((is_prime(int(s[i:])) and is_prime(int(s[:len(s) - i])) for i in range(len(s)))):
        return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[67]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)