def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if num % 10 == 0:
        return False
    if not is_prime(num):
        return False
    return is_truncatable_prime(num // 10)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True