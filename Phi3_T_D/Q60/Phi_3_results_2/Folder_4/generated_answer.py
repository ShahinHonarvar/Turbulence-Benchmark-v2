def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes_set):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True if n in primes_set else False

def all_left_right_truncatable_prime(tuples):
    primes_set = set(filter(is_prime, range(10, tuples[96] + 1)))
    return sorted([x for x in range(3, tuples[96] + 1) if x not in primes_set and is_truncatable_prime(x, primes_set)], reverse=True)