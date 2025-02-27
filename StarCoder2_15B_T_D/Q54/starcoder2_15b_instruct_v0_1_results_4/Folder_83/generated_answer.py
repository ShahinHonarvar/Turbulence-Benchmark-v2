def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[24]
    result = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(1, len(str(i))):
            if not is_prime(int(str(i)[:-j])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            result.append(i)
    result.sort()
    return result