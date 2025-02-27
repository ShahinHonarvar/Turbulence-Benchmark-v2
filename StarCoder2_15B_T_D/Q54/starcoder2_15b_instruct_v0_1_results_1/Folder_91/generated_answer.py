def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        truncatable_primes = []
        for i in range(1, len(str(x)) + 1):
            truncated_number = int(str(x)[:i])
            if is_prime(truncated_number):
                truncatable_primes.append(truncated_number)
        if len(truncatable_primes) > 0:
            result.append(sorted(truncatable_primes, reverse=True))
    return result