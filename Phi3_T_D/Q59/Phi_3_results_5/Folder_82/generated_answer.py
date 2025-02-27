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
    x = numbers[69]
    left_truncatable_primes = []
    for prime in range(x - 1, 7, -1):
        str_prime = str(prime)
        if prime > 10 and all((is_prime(int(str_prime[i:])) for i in range(len(str_prime)))):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes