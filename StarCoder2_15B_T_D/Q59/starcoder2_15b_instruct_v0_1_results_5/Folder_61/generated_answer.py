def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[3]
    result = []
    for i in range(1, x):
        if is_prime(i):
            truncatable = True
            for j in range(len(str(i)) - 1):
                if not is_prime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)