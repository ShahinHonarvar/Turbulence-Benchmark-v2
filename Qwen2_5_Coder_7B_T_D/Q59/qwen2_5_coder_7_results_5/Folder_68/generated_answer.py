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
    x = t[1]
    primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                left_truncatable = False
                break
        if left_truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)