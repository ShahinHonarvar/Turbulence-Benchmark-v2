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

def all_right_truncatable_primes(numbers):
    x = numbers[67]
    right_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        if is_prime(n) and all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1))):
            right_truncatable_primes.append(n)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes