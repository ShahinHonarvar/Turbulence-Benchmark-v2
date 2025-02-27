import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[69]
    rtp = []
    for i in range(2, x):
        num = i
        while num > 0:
            if is_prime(num):
                rtp.append(num)
                break
            num //= 10
    rtp.sort(reverse=True)
    return rtp