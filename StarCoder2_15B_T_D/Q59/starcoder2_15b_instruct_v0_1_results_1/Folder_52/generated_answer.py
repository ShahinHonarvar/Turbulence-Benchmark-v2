def all_left_truncatable_prime(t):
    x = t[52]
    result = []
    for i in range(1, x):
        is_left_truncatable_prime = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True