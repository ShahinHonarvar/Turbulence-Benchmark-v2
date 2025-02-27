def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    truncatable_primes = []
    for p in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(p)) - 1):
            truncated_left = int(str(p)[i + 1:])
            truncated_right = int(str(p)[:-i - 1])
            if not is_prime(truncated_left) or not is_prime(truncated_right):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True