def all_left_truncatable_prime(t):
    x = t[26]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n in [0, 1]:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        while p > 0:
            if p % 10 == 0:
                return False
            if not is_prime(p):
                return False
            p //= 10
        return True
    result = []
    for num in range(10, x):
        if is_prime(num) and is_left_truncatable(num):
            result.append(num)
    return sorted(result)