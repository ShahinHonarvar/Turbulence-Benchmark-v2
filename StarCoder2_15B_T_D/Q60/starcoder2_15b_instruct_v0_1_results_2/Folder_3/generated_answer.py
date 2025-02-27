import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_positive_integers):
    left_right_truncatable_primes = []
    for x in tuple_of_positive_integers:
        if is_prime(x):
            num_str = str(x)
            while len(num_str) > 1:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[1:]
            if len(num_str) == 1 and is_prime(int(num_str)):
                left_right_truncatable_primes.append(x)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes