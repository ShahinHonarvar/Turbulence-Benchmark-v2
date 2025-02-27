def all_left_truncatable_prime(numbers):
    x = numbers[71]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(1, len(str(i))):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True