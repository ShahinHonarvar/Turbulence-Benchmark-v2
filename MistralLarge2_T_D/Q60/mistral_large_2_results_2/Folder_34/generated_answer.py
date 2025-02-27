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
    num_str = str(n)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if not is_prime(int(num_str)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[18]
    truncatable_primes = [n for n in range(10, x + 1) if is_left_right_truncatable(n)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes