def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[18]
    truncatable_primes = []
    for i in range(x, 1, -1):
        s = str(i)
        if not all((c in '123456789' for c in s)):
            continue
        if all((is_prime(int(s[:n])) for n in range(1, len(s)))) and all((is_prime(int(s[n:])) for n in range(len(s)))):
            truncatable_primes.append(i)
    return truncatable_primes