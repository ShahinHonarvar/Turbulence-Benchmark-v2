import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[32]
    result = []
    for i in range(10, x + 1):
        if is_prime(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                left_trunc = int(str(i)[j:])
                right_trunc = int(str(i)[:-j])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(i)
    return sorted(result)