def all_left_right_truncatable_prime(tup):
    x = tup[36]
    left_right_truncatable_primes = []
    for potential_prime in range(2, x + 1):
        if is_prime(potential_prime):
            if is_left_right_truncatable_prime(potential_prime):
                left_right_truncatable_primes.append(potential_prime)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if n % 10 == 0:
        return False
    if not is_prime(n):
        return False
    return is_left_right_truncatable_prime(n // 10)