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
    x = numbers[100]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    left_truncatable = []
    for prime in primes:
        if all((is_prime(int(prime[1:i + 1])) for i in range(len(prime)))):
            left_truncatable.append(int(prime))
    return left_truncatable