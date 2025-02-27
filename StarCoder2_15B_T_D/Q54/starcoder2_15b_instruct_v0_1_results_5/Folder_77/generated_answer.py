import math

def all_right_truncatable_prime(tup):
    x = tup[767]
    prime_list = []
    for i in range(2, x):
        if is_prime(i):
            prime_list.append(i)
    right_truncatable_prime_list = []
    for prime in prime_list:
        is_right_truncatable = True
        truncated_prime = prime
        while truncated_prime > 0:
            if not is_prime(truncated_prime):
                is_right_truncatable = False
                break
            truncated_prime //= 10
        if is_right_truncatable:
            right_truncatable_prime_list.append(prime)
    right_truncatable_prime_list.sort(reverse=True)
    return right_truncatable_prime_list

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True