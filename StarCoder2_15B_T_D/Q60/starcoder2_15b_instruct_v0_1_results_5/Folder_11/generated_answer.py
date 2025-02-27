def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[86]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            is_truncatable = True
            for j in range(1, len(str(i))):
                left_truncatable = int(str(i)[j:])
                right_truncatable = int(str(i)[:-j])
                if not is_prime(left_truncatable) or not is_prime(right_truncatable):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True