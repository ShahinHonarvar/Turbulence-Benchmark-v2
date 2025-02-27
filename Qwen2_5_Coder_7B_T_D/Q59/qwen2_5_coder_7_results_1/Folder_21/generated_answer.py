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

def all_left_truncatable_prime(numbers):
    x = numbers[175]
    left_truncatable_primes = []
    for num in range(2, x):
        if str(num).count('0') == 0 and all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)