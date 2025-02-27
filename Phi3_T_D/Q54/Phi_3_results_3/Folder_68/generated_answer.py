def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_truncations(n):
    str_n = str(n)
    for i in range(len(str_n)):
        yield int(str_n[:i] + str_n[i + 1:])

def is_right_truncatable_prime(n):
    for truncation in all_truncations(n):
        if not is_prime(truncation):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[1]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)