def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    pr = str(n)
    while pr:
        if not is_prime(int(pr)):
            return False
        pr = pr[:-1]
    return True

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[74]
    primes = set()
    right_truncatable_primes = []
    for number in range(2, x):
        if is_prime(number):
            primes.add(number)
            if is_right_truncatable_prime(number, primes):
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)