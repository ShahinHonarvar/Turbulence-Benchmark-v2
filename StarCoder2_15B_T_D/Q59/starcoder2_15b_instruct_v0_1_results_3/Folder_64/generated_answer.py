import math

def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[4]
    is_prime_cache = [True] * x
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime_cache[i]:
            for j in range(i * i, x, i):
                is_prime_cache[j] = False
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime_cache[i]:
            is_left_truncatable = True
            remaining_number = i
            while remaining_number >= 1:
                last_digit = remaining_number % 10
                if last_digit == 0:
                    is_left_truncatable = False
                    break
                remaining_number //= 10
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)