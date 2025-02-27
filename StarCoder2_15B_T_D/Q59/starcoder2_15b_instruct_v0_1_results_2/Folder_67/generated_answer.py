import math

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x, i):
                is_prime[j] = False
    left_truncatable_primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            is_left_truncatable = True
            temp = i
            while temp > 0:
                if not is_prime[temp]:
                    is_left_truncatable = False
                    break
                temp //= 10
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes