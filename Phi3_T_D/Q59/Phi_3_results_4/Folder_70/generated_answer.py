def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(num, x):
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[432]
    left_truncatable_primes = [num for num in range(3, x, 2) if is_left_truncatable(num, x)]
    return sorted(left_truncatable_primes, reverse=True)