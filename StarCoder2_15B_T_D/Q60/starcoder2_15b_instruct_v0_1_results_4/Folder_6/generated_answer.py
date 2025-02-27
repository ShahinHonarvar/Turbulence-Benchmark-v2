def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[74]
    left_right_truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])) or not is_prime(int(str(i)[:-j])):
                    truncatable = False
                    break
            if truncatable:
                left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes