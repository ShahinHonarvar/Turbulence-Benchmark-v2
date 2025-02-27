def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(prime):
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for num in range(23, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes