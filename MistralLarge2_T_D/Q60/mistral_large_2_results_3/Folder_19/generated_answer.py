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
    if not is_prime(n):
        return False
    if '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        if not is_prime(int(s[1:])) or not is_prime(int(s[:-1])):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[67]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)