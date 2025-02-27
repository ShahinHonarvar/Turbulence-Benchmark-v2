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

def right_truncatable_prime(prime, primes_set):
    if prime == 0 or prime == 1:
        return True
    return all((right_truncatable_prime(int(str(prime)[:-i]), primes_set) for i in range(1, len(str(prime)))))

def all_left_truncatable_prime(numbers):
    x = numbers[28]
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatables = [prime for prime in primes if right_truncatable_prime(prime, set(primes))]
    return sorted(left_truncatables)