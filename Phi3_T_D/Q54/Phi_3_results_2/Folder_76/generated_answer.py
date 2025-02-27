def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_primes_less_than(n):
    primes = [str(i) for i in range(2, n) if is_prime(i)]
    right_truncatable_primes = []
    for p in primes:
        while p:
            if not is_prime(int(p)):
                break
            right_truncatable_primes.append(int(p))
            p = p[:-1]
    return right_truncatable_primes[::-1]

def all_right_truncatable_prime(tup):
    x = tup[370]
    return all_right_truncatable_primes_less_than(x)