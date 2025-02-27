def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        digits = str(prime)
        for i in range(len(digits)):
            truncated_number = int(digits[i:])
            if not is_prime(truncated_number):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True