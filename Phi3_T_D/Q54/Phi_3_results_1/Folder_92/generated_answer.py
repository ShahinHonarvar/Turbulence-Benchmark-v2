def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    if n < 10:
        return is_prime(n) and n in primes
    return is_prime(n) and is_right_truncatable_prime(n // 10, primes)

def all_right_truncatable_prime(numbers):
    x = numbers[7]
    primes = [2, 3, 5, 7]
    right_truncatables = []
    for num in range(2, x):
        if is_right_truncatable_prime(num, primes):
            right_truncatables.append(num)
    return sorted(right_truncatables)