def all_left_truncatable_prime(numbers):
    numbers = list(numbers)
    x = numbers[94]
    left_truncatable_primes = []
    for prime in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(prime))):
            truncated_prime = int(str(prime)[i:])
            if not is_prime(truncated_prime):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True