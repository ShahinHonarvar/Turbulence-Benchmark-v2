import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[69]
    result = []
    for n in range(1, x):
        if is_prime(n):
            for i in range(len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    break
            else:
                result.append(n)
    return sorted(result, reverse=True)