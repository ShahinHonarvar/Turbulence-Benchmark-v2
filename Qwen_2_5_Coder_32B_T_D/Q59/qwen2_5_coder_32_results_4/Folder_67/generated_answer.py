def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[71]
    left_trunc_primes = []
    for num in range(2, x):
        snum = str(num)
        if '0' not in snum and all((is_prime(int(snum[i:])) for i in range(len(snum)))):
            left_trunc_primes.append(num)
    return sorted(left_trunc_primes, reverse=True)