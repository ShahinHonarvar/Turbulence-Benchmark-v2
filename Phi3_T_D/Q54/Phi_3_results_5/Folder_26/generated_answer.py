def is_prime(n):
    if n <= 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(len(str_n), 0, -1):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    trunc_primes = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(trunc_primes, reverse=True)