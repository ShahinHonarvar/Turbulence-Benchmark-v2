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

def is_truncatable_prime(n, primes):
    s = str(n)
    for i in range(1, len(s)):
        if not (is_prime(int(s[i:])) and int(s[:i]) in primes):
            return False
    return True

def left_and_right_truncatable_primes(primes, n):
    return [p for p in primes if is_truncatable_prime(p, primes)]

def get_primes_up_to(limit):
    primes = [2]
    for possiblePrime in range(3, limit + 1, 2):
        if is_prime(possiblePrime):
            primes.append(possiblePrime)
    return primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    primes = get_primes_up_to(x)
    truncatable_primes = left_and_right_truncatable_primes(primes, primes[len(primes) - 1])
    truncatable_primes.sort(reverse=True)
    return truncatable_primes