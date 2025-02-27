def all_left_right_truncatable_prime(tuple_of_positive_integers):
    left_right_truncatable_primes = []
    for prime in tuple_of_positive_integers:
        is_left_right_truncatable = True
        str_prime = str(prime)
        for i in range(len(str_prime)):
            truncated_prime = int(str_prime[i:])
            if not is_prime(truncated_prime):
                is_left_right_truncatable = False
                break
            truncated_prime = int(str_prime[:len(str_prime) - i])
            if not is_prime(truncated_prime):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True