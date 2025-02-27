def is_prime(n):
    """Check if the number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[30]
    truncatable_primes = []

    def is_truncatable_prime(n, seen):
        if n < 10 and n in {2, 3, 5, 7}:
            return True
        str_n = str(n)
        if any((digit == '0' for digit in str_n)):
            return False
        return all((is_prime(int(str_n[i + 1:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num, set()):
            truncatable_primes.append(num)
    return truncatable_primes