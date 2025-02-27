def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_truncatable_right_primes(n, acc=None):
    if acc is None:
        acc = []
    if n < 10:
        if is_prime(n):
            acc.append(n)
        return sorted(acc, reverse=True)
    if is_prime(n):
        acc.append(n)
    return all_truncatable_right_primes(n // 10, acc)

def all_right_truncatable_prime(*args):
    return all_truncatable_right_primes(args[0][0])