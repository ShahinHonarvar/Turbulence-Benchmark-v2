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

def is_left_truncatable_prime(n, b=10):
    s, i = (str(n), len(str(n)))
    for count in range(i):
        if not is_prime(int(s[count:], b)):
            return False
    return True

def all_left_truncatable_prime(numbers, index=64):
    x = numbers[index]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)