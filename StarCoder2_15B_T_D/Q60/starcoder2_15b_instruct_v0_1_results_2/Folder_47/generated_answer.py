def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    left_truncatable_primes = []
    right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and i not in left_truncatable_primes:
            left_truncatable_primes.append(i)
    while left_truncatable_primes:
        prime = left_truncatable_primes.pop()
        if prime > 10:
            last_digit = prime % 10
            if last_digit != 0 and is_prime(prime // 10):
                right_truncatable_primes.append(prime)
            else:
                continue
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)