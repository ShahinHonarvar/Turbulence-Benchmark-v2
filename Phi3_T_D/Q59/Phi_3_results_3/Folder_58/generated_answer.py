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

def left_truncatable_prime(n):
    n_str = str(n)
    while len(n_str) > 1 and is_prime(int(n_str)):
        n_str = n_str[1:]
    return is_prime(n)

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    truncable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and left_truncatable_prime(i):
            truncable_primes.append(i)
    return truncable_primes