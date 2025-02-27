def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(number, primes):
    str_num = str(number)
    for i in range(len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def all_left_truncatable_primes(range_end):
    primes = [n for n in range(2, range_end) if is_prime(n)]
    return [p for p in primes if is_left_truncatable(p, primes)][::-1]