def all_right_truncatable_prime(numbers):
    x = numbers[38]
    right_truncatable_primes = []
    for num in range(2, x):
        if all((is_prime(int(num[-(i + 1):])) for i in range(len(num)))):
            right_truncatable_primes.append(int(num))
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True