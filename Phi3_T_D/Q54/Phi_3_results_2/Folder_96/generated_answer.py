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

def is_right_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_right_truncatable_prime(int_tuple):
    x = int_tuple[29]
    right_truncatables = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable_prime(num, right_truncatables):
            right_truncatables.append(num)
    return sorted(right_truncatables)