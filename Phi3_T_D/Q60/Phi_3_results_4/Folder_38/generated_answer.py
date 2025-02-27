def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [prime for prime in primes if is_truncatable_prime(prime, primes)]
    return truncatable_primes