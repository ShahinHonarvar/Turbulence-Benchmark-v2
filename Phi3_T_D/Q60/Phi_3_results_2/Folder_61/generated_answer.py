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

def is_truncatable(n, primes):
    if not all((digit != '0' for digit in str(n))) or n not in primes:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    primes = set()
    for i in range(2, x + 1):
        if is_prime(i):
            primes.add(i)
    left_right_primes = [p for p in primes if is_truncatable(p, primes)]
    return sorted(left_right_primes, reverse=True)