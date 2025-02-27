def all_right_truncatable_prime(tup):
    x = tup[14]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable = True
        for j in range(len(str(i)) - 1, 0, -1):
            if not is_prime(int(str(i)[:j])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True