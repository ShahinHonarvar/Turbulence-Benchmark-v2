import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[84]
    result = []
    for n in range(1, x + 1):
        if is_prime(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(n)
    result.sort(reverse=True)
    return result