def is_right_truncatable_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return is_right_truncatable_prime(n // 10)

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    right_truncatable_primes = []
    for n in range(1, x):
        if is_right_truncatable_prime(n):
            right_truncatable_primes.append(n)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes