def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[8]
    result = []
    for i in range(1, x):
        if is_prime(i) and all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            result.append(i)
    return sorted(result, reverse=True)