import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[43]
    rt_primes = []
    for i in range(2, x):
        is_rt_prime = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_rt_prime = False
                break
        if is_rt_prime:
            rt_primes.append(i)
    rt_primes.sort()
    return rt_primes