def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
            return False
    return True

def all_left_and_right_truncatable_primes(numbers):
    x = numbers[61]
    truncatable_primes = [i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)]
    return truncatable_primes