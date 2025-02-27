def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if not is_prime(n):
        return False
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    if x < 10:
        return []
    for num in range(10, x):
        if is_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)