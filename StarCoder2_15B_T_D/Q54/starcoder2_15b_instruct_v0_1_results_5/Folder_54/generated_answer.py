import math

def all_right_truncatable_prime(t):
    x = t[88]
    is_prime = [True] * x
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    right_truncatable_primes = set()
    for i in range(2, x):
        if is_prime[i]:
            right_truncatable_primes.add(i)
            for j in range(1, len(str(i))):
                if not is_prime[int(str(i)[:-j])]:
                    right_truncatable_primes.discard(i)
                    break
    return sorted(list(right_truncatable_primes), reverse=True)