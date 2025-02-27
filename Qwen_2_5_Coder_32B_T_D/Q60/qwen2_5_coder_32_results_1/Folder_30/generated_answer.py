def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[37]
    lr_truncatable_primes = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' not in s:
            all_prime = True
            l, r = (num, num)
            for _ in range(len(s) - 1):
                l, r = (int(s[1:]), int(s[:-1]))
                if not is_prime(l) or not is_prime(r):
                    all_prime = False
                    break
                s = s[1:-1]
            if all_prime and is_prime(l):
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)