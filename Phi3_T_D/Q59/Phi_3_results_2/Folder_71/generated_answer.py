def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, base=10):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_primes(numbers):
    x = numbers[22]
    primes = []
    candidate = 10
    while candidate < x:
        if is_prime(candidate) and is_left_truncatable(candidate):
            primes.append(candidate)
        candidate += 1
    return sorted(primes, reverse=True)