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

def is_right_truncatable_prime(n, primes):
    return all((is_prime(int(n[i:])) for i in range(1, len(n))))

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(str(p), primes)]
    return sorted(right_truncatable_primes, reverse=True)