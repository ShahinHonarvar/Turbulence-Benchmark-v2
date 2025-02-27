def is_truncatable_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)