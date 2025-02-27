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
    x = t[175]
    ltp = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        truncatable = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                truncatable = False
                break
        if truncatable:
            ltp.append(num)
    return sorted(ltp)