def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes_set):
    return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))

def all_left_truncatable_prime(numbers):
    x = numbers[758]
    primes = set()
    for y in range(2, x):
        if is_prime(y) and is_left_truncatable_prime(y, primes):
            primes.add(y)
    return sorted(primes)