def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(prime):
    if prime < 10:
        return False
    str_prime = str(prime)
    return all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:i])) for i in range(1, len(str_prime))))

def all_left_right_truncatable_primes(numbers):
    x = numbers[8]
    result = []
    for prime in reversed(range(2, x + 1)):
        if is_truncatable(prime):
            result.append(prime)
    return result