def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    right_truncatable_primes = []

    def is_right_truncatable(number):
        return all((is_prime(int(str(number)[:-i])) and len(str(number)[:-i]) > 0 for i in range(1, len(str(number)) + 1)))
    for num in range(2, x):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)