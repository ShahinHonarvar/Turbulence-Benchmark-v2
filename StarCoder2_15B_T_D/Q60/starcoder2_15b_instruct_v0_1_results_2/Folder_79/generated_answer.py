def all_left_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[91]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        num_digits = len(str(prime))
        for i in range(1, num_digits):
            left_truncation = prime // 10 ** i
            right_truncation = prime % 10 ** i
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True