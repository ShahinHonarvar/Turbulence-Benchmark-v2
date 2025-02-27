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
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 27:
        return []
    limit = numbers[26]
    primes = [2]
    for num in range(3, limit, 2):
        if is_prime(num):
            primes.append(num)
    right_truncatable_primes = [prime for prime in primes if is_right_truncatable_prime(prime, primes)]
    return sorted(right_truncatable_primes)