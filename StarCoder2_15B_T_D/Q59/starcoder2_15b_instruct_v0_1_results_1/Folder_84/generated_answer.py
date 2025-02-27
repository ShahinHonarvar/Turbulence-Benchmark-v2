def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []

    def helper(n):
        if n == 0:
            return True
        for i in range(1, 10):
            if is_prime(n) and helper(n % 10 ** i):
                result.append(n)
                return True
        return False
    helper(x)
    return sorted(result, reverse=True)