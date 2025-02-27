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

def all_left_truncatable_prime(tup):
    x = tup[86]
    result = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            is_left_truncatable = True
            for j in range(len(s)):
                if not is_prime(int(s[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(i)
    return sorted(result)