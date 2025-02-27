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

def right_truncatable(n, prime_set):
    n_str = str(n)
    if n < 10 or len(prime_set) == 0:
        return n in prime_set
    return all((is_prime(int(n_str[:-i])) for i in range(1, len(n_str)))) and n in prime_set

def all_right_truncatable_prime(numbers):
    primes = [i for i in range(2, numbers[29]) if is_prime(i)]
    return sorted([p for p in primes if right_truncatable(p, set(primes))])