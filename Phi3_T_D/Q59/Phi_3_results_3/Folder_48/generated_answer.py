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

def all_left_truncatable_prime(t):
    x = t[835]
    primes = []
    s = 10
    while s < x:
        if is_prime(s):
            s_str = str(s)
            can_truncate = True
            for i in range(len(s_str)):
                if not is_prime(int(s_str[i:])):
                    can_truncate = False
                    break
            if can_truncate:
                primes.append(s)
        s += 1
    return primes