def is_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    s = str(n)
    if '0' in s:
        return False
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[126]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)