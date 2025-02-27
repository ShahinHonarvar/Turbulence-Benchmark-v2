def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(prime)) - 1):
            truncated_prime = int(str(prime)[i + 1:])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
            truncated_prime = int(str(prime)[:-i - 1])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True