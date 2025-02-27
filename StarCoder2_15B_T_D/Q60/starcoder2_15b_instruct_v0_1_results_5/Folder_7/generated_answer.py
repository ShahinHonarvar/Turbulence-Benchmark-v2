def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for x in numbers:
        if x >= 10:
            left_truncatable = is_left_truncatable_prime(x)
            right_truncatable = is_right_truncatable_prime(x)
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(x)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes

def is_left_truncatable_prime(x):
    while x >= 10:
        if not is_prime(x):
            return False
        x //= 10
    return is_prime(x)

def is_right_truncatable_prime(x):
    while x >= 10:
        if not is_prime(x):
            return False
        x = int(str(x)[:-1])
    return is_prime(x)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True