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

def is_truncatable_prime(p):
    s = str(p)
    return all((is_prime(int(s[:i])) for i in range(1, len(s)))) and all((is_prime(int(s[i:])) for i in range(1, len(s))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)