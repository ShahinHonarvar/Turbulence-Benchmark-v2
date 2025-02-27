def all_right_truncatable_prime(numbers):
    x = numbers[618]
    truncatable_primes = []
    for prime in range(2, x):
        is_truncatable = True
        for i in range(1, len(str(prime))):
            truncated_number = int(str(prime)[:-i])
            if not is_prime(truncated_number):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True