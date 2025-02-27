def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[630]
    results = []
    for i in range(2, x):
        num = i
        while num % 10 != num:
            if not is_prime(num):
                break
            num //= 10
        if num == 0:
            results.append(i)
    return sorted(results, reverse=True)