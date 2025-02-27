def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[77]
    lrt_primes = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_trunc = True
        right_trunc = True
        for i in range(1, len(s)):
            if not all((is_prime(int(s[i:])) for i in range(i, len(s)))) or not all((is_prime(int(s[:len(s) - i])) for i in range(1, len(s)))):
                left_trunc = False
                right_trunc = False
                break
        if left_trunc and right_trunc and is_prime(num):
            lrt_primes.append(num)
    return sorted(lrt_primes)