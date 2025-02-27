def all_left_truncatable_prime(numbers):
    x = numbers[22]
    left_truncatable_primes = []
    for prime in range(2, x):
        is_left_truncatable = True
        truncated_number = prime
        while truncated_number > 0:
            if not is_prime(truncated_number):
                is_left_truncatable = False
                break
            truncated_number //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)

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