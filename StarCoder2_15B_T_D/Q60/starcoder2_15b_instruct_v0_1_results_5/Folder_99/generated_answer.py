def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[758]
    left_right_truncatable_primes = []
    for prime in range(2, x + 1):
        is_left_right_truncatable = True
        truncated_prime = prime
        while len(str(truncated_prime)) > 1:
            if not is_prime(truncated_prime):
                is_left_right_truncatable = False
                break
            truncated_prime = int(str(truncated_prime)[1:])
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))