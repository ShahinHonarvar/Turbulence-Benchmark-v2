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
    str_n = str(n)
    if len(str_n) == 1 or len(str_n) == 2:
        return is_prime(n)
    for i in range(len(str_n) - 1):
        if is_prime(n % 10 ** (i + 1)) == False or is_prime(n // 10 ** (len(str_n) - i - 1)) == False:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    truncatable_primes = []
    n = 10
    while n <= x:
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
        n += 1
    return sorted(truncatable_primes)