def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[433]
    primes = []
    for num in range(2, x):
        temp = num
        while temp:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            primes.append(num)
    return sorted(primes, reverse=True)