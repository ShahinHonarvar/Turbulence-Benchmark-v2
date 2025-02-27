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

def right_truncatable_prime(n):
    n_str = str(n)
    while n > 0:
        if not is_prime(n):
            return False
        n = int(n_str[:-1])
        n_str = n_str[:-1]
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    return sorted([i for i in range(2, x) if is_prime(i) and right_truncatable_prime(i)], reverse=True)