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

def is_left_truncatable_prime(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    while num_str:
        if not is_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True

def all_left_truncatable_prime(t):
    x = t[33]
    primes = []
    num = 2
    while num < x:
        if is_left_truncatable_prime(num):
            primes.append(num)
        num += 1
    return sorted(primes)