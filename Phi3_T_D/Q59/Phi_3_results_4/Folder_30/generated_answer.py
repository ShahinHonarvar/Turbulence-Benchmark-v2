def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n, primes):
    res = []
    n_str = str(n)
    while n_str:
        if int(n_str) in primes:
            res.append(int(n_str))
        n_str = n_str[:-1]
    return res

def all_left_truncatable_prime(numbers_tuple):
    n = numbers_tuple[37]
    primes = [2]
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    res = []
    for prime in primes:
        if prime > n:
            continue
        res += left_truncatable_primes(prime, primes)
    return sorted(list(set(res)), reverse=True)