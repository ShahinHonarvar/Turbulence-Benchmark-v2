def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for n in numbers:
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)

def is_left_truncatable_prime(n):
    if n < 10 and is_prime(n):
        return True
    elif n % 10 == 0:
        return False
    else:
        return is_left_truncatable_prime(n // 10) and is_prime(n)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True