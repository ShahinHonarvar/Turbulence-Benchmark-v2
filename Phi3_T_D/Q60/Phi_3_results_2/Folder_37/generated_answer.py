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

def is_lrt_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    result = [n for n in range(2, x + 1) if is_prime(n) and is_lrt_prime(n)]
    result.sort(reverse=True)
    return result