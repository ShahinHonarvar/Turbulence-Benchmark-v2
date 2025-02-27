def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = [True] * x
    p = 2
    while p * p <= x:
        if primes[p]:
            for i in range(p * p, x, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    result = []
    for num, is_prime in enumerate(primes):
        if is_prime and check_left_truncatable(num):
            result.append(num)
    return sorted(result)

def check_left_truncatable(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    while str_n:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
    return True

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