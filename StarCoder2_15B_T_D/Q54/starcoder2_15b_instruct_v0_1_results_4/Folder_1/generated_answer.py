def is_right_truncatable_prime(n):
    s = str(n)
    while len(s) > 0:
        if not is_prime(int(s)):
            return False
        s = s[:-1]
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[20]
    result = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            result.append(n)
    result.sort(reverse=True)
    return result