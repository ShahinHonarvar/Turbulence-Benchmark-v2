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

def is_truncatable_prime(prime):
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    truncatables = []
    for i in range(x, 0, -1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatables.append(i)
    return truncatables