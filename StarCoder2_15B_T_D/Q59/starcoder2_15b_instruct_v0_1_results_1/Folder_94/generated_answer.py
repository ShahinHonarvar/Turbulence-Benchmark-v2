def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    results = []
    for i in range(2, x):
        if is_prime(i):
            results.append(i)
    return results