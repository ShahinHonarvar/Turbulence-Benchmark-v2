def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[61]
    lr_trunc_primes = []
    for num in range(11, x + 1):
        snum = str(num)
        if '0' in snum:
            continue
        l = snum
        r = snum
        is_lr_trunc_prime = True
        while len(l) > 1:
            l = l[1:]
            r = r[:-1]
            if not is_prime(int(l)) or not is_prime(int(r)):
                is_lr_trunc_prime = False
                break
        if is_lr_trunc_prime and is_prime(num):
            lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes)