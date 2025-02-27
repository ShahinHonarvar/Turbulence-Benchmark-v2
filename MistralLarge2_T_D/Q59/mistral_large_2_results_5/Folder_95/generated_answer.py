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
    x = t[77]
    primes = []
    for num in range(2, x):
        if not is_prime(num) or '0' in str(num):
            continue
        num_str = str(num)
        is_left_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            primes.append(num)
    return sorted(primes)