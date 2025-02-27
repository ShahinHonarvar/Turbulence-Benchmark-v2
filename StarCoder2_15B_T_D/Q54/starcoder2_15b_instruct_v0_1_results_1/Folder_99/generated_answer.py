import math

def all_right_truncatable_prime(tup):
    x = tup[758]
    is_prime = [True] * x
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    right_truncatable_primes = []
    for i in range(10, x):
        if is_prime[i]:
            right_truncatable = True
            for j in range(len(str(i)) - 1):
                if not is_prime[int(str(i)[:-j - 1])]:
                    right_truncatable = False
                    break
            if right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)