def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[36]
    if x < 11:
        return []
    lrt_primes = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        is_lrt = True
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:-i])) or not is_prime(int(s[:i])) or (not is_prime(int(s[:-i]))):
                is_lrt = False
                break
        if is_lrt and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
            lrt_primes.append(num)
    return sorted(lrt_primes, reverse=True)