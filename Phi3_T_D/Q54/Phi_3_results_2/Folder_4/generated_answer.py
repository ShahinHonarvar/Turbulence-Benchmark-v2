def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes(min_len, current_value, truncatables):
    if min_len == 1:
        return
    for i in range(10, 0, -1):
        next_value = current_value * 10 + i
        if is_prime(next_value):
            truncatables.append(next_value)
            generate_right_truncatable_primes(min_len - 1, next_value, truncatables)

def all_right_truncatable_prime(bound):
    valid_primes = []
    for i in range(2, 10):
        generate_right_truncatable_primes(bound[96] // i, i, valid_primes)
    return sorted(filter(is_prime, valid_primes), reverse=True)