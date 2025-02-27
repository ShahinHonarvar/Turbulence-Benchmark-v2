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

def is_left_right_truncatable_prime(n, primes_set):
    if n == 0 or n == 2:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or (i > 0 and (not is_prime(int(str_n[:i])))):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[67]
    primes = [2, 3, 5, 7]
    num = 11
    while num <= x:
        if is_prime(num) and is_left_right_truncatable_prime(num, set(primes)):
            primes.append(num)
        num += 2
    return sorted(primes, reverse=True)