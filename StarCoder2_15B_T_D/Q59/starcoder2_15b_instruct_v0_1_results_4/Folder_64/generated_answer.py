def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[4]
    ltp = []
    for p in range(2, x):
        if is_prime(p):
            truncatable = True
            for i in range(len(str(p)) - 1):
                if not is_prime(int(str(p)[i:])):
                    truncatable = False
                    break
            if truncatable:
                ltp.append(p)
    return sorted(ltp)