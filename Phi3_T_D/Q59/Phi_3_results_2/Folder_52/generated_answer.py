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

def is_left_truncatable_prime(n, prime_cache={}):
    if n in prime_cache:
        return prime_cache[n]
    if is_prime(n):
        if n < 10 or all((is_left_truncatable_prime(int(n[i:]), prime_cache) for i in range(1, len(n)))):
            prime_cache[n] = True
            return True
    prime_cache[n] = False
    return False

def all_left_truncatable_prime(number_tuple):
    x = number_tuple[52]
    truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(str(num)):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes