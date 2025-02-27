def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    while n > 0:
        if n not in sieve or not is_prime(n):
            return False
        n = n % 100 // 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[0]
    sieve = set((prime for prime in range(2, x) if is_prime(prime)))
    left_truncatable_primes = [prime for prime in sieve if is_left_truncatable_prime(prime, sieve)]
    return left_truncatable_primes[::-1]