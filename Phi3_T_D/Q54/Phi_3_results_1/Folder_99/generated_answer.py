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

def right_truncatable_prime(n):
    primes = [str(i) for i in range(2, n + 1) if is_prime(i)]
    return all((is_prime(int(p[:-1])) for p in primes if len(p) > 1))

def all_right_truncatable_prime(numbers):
    x = numbers[758]
    primes_list = right_truncatable_prime(x)
    return primes_list