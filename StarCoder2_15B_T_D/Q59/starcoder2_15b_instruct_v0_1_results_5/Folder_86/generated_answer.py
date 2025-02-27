def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[126]
    result = []
    for n in range(2, x):
        if is_prime(n):
            is_left_truncatable = True
            for i in range(len(str(n)) - 1):
                if not is_prime(int(str(n)[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(n)
    return sorted(result, reverse=True)