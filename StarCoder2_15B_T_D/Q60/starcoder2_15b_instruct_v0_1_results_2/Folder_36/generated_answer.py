def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[992]
    left_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            left_truncatable_primes.append(i)
    right_truncatable_primes = []
    for i in left_truncatable_primes:
        is_right_truncatable = True
        while i >= 10:
            i = i // 10
            if not is_prime(i):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)