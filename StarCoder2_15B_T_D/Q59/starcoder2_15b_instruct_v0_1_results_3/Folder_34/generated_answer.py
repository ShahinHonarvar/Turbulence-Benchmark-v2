def all_left_truncatable_prime(x):
    if x is None or len(x) == 0:
        return []
    prime_numbers = []
    for i in range(2, x[18]):
        if is_prime(i):
            prime_numbers.append(i)
    left_truncatable_prime_numbers = []
    for prime in prime_numbers:
        is_left_truncatable = True
        truncated_prime = prime
        while truncated_prime > 0:
            if not is_prime(truncated_prime):
                is_left_truncatable = False
                break
            truncated_prime //= 10
        if is_left_truncatable:
            left_truncatable_prime_numbers.append(prime)
    return sorted(left_truncatable_prime_numbers, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True