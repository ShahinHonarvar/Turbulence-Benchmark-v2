def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[49]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            original = i
            is_left_truncatable = True
            while is_left_truncatable and original > 0:
                original = int(str(original)[1:])
                if not is_prime(original):
                    is_left_truncatable = False
            if is_left_truncatable:
                truncatable_primes.append(i)
    return truncatable_primes