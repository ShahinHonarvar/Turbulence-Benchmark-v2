def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    str_n = str(n)
    if not is_prime(n):
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def generate_truncable_primes(limit):
    truncable_primes = []
    current_prime = 11
    while current_prime <= limit:
        if is_left_right_truncatable(current_prime):
            truncable_primes.append(current_prime)
        current_prime += 2
    return truncable_primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    return generate_truncable_primes(x)