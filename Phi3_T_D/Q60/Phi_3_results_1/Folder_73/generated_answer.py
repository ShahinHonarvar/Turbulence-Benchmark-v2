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

def is_left_right_truncatable(n):
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    temp = n
    while temp > 9:
        temp = int(str(temp)[:-1])
        if not is_prime(temp):
            return False
    return True

def all_left_right_truncatable_prime(*args):
    x = args[97] if 97 < len(args) else 0
    return [i for i in range(2, x + 1) if is_left_right_truncatable(i)]