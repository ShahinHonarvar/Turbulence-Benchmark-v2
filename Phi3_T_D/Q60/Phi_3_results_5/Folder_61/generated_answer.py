def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(prime):
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    truncatable_primes = [i for i in range(23, x + 1) if is_prime(i) and is_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)