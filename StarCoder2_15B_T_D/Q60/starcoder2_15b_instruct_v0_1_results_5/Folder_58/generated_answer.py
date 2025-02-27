def is_truncatable(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable(int(str(n)[1:])) and is_truncatable(int(str(n)[:-1]))

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
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
    result = []
    for n in numbers:
        if is_truncatable(n):
            result.append(n)
    result.sort(reverse=True)
    return result