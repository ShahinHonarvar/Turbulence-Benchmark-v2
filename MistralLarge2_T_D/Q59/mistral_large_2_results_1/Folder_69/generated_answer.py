def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    while str_num:
        if not is_prime(int(str_num)):
            return False
        str_num = str_num[1:]
    return True

def all_left_truncatable_prime(tpl):
    x = tpl[760]
    primes = []
    for i in range(2, x):
        if is_left_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)