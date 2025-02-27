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

def is_right_truncatable_prime(prime):
    while prime > 0:
        if not is_prime(prime):
            return False
        prime //= 10
    return True

def generate_primes_below(x):
    primes = []
    for possible_prime in range(2, x):
        if is_prime(possible_prime):
            primes.append(possible_prime)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    primes_below_x = generate_primes_below(x)
    right_truncatable_primes = [p for p in primes_below_x if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes)