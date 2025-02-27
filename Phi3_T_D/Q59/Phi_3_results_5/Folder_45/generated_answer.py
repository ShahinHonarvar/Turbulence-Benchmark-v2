def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    str_n = str(n)
    while len(str_n) > 1 and is_prime(int(str_n)):
        str_n = str_n[1:]
    return len(str_n) == 1

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    return sorted([n for n in range(2, x) if left_truncatable_prime(n)])