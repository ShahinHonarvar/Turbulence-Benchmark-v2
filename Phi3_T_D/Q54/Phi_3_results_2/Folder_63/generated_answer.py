def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    candidate_primes = [2, 3, 5, 7]
    primes = candidate_primes.copy()
    for num in range(11, x, 2):
        if is_prime(num):
            primes.append(num)
    return [p for p in primes if is_right_truncatable_prime(p, primes)][:x] if x > 7 else []