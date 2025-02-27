import math

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    right_truncatable_primes = []
    for i in range(x):
        if is_prime[i]:
            is_right_truncatable = True
            temp = i
            while temp > 0:
                if not is_prime[temp]:
                    is_right_truncatable = False
                    break
                temp //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)