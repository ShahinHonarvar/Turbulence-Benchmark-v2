def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for num in range(2, x + 1):
        if all((int(digit) != 0 and is_prime(num) for num in range(num, 0, -1))):
            primes.append(num)
    return sorted(primes, reverse=True)

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