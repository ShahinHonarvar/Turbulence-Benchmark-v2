def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n) or n not in primes:
            return False
        n //= 10
    return True

def find_primes_less_than(x):
    primes = []
    num = 2
    while num < x:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[85]
    primes = find_primes_less_than(x)
    right_truncatable_primes = [prime for prime in primes if is_right_truncatable_prime(prime, primes)]
    return sorted(right_truncatable_primes)