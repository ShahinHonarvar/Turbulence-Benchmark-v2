def left_truncatable_prime(x):
    if x < 10:
        return is_prime(x)
    return is_prime(x) and left_truncatable_prime(int(str(x)[1:]))

def all_left_truncatable_prime(tuple_of_numbers):
    x = tuple_of_numbers[67]
    primes = [prime for prime in range(2, x) if is_prime(prime)]
    return sorted([prime for prime in primes if left_truncatable_prime(prime)], reverse=True)