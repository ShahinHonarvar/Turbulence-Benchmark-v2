import math

def all_right_truncatable_prime(t):
    x = t[28]
    is_prime = [True] * x
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    right_truncatable_primes = []
    for i in range(x):
        if is_prime[i]:
            is_right_truncatable = True
            for j in range(len(str(i)) - 1):
                if not is_prime[int(str(i)[:-j - 1])]:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)