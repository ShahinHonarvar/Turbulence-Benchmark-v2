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

def left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:]
        str_n = str_n[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [p for p in primes if left_right_truncatable_prime(p)]
    return sorted(left_right_truncatable_primes, reverse=True)