def all_left_truncatable_prime(t):
    x = t[42]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(len(str(i))):
            truncated_num = int(str(i)[j:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

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