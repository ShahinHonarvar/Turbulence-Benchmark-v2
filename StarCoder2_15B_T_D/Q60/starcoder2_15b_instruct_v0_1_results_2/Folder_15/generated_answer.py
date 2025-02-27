def is_truncatable_prime(x):
    s = str(x)
    for i in range(len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True