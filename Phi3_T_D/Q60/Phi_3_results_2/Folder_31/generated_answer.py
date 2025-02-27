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

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return primes[::-1]