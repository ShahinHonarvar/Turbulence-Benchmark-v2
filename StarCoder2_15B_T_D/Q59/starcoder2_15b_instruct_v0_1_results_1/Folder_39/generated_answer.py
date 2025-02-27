def all_left_truncatable_prime(numbers):
    x = numbers[30]
    left_truncatable_primes = []
    for n in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(n)) - 1):
            truncated_number = int(str(n)[i + 1:])
            if not is_prime(truncated_number):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True