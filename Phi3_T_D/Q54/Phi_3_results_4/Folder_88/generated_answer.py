def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    right_truncatable_primes = []
    x = numbers_tuple[93]
    for num in range(2, x):
        if is_prime(num):
            original = num
            is_truncatable = True
            while original > 0:
                original = int(str(original)[:-1])
                if not is_prime(original):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)