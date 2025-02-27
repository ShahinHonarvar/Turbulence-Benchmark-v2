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

def left_and_right_truncatable_prime(x):
    primes = set()
    for n in range(2, x + 1):
        if is_prime(n):
            str_n = str(n)
            left_truncatable = all((is_prime(int(str_n[i:])) for i in range(len(str_n))))
            right_truncatable = all((is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))
            if left_truncatable and right_truncatable:
                primes.add(n)
    return sorted(primes, reverse=True)

def all_left_right_truncatable_prime(t):
    x = t[3]
    return left_and_right_truncatable_prime(x)